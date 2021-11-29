"""
mavedb.base
~~~~~~~~~~~

Handles interface between the user and MaveDB.
"""

import functools
import urllib
from posixpath import join as urljoin

import requests


class BaseAPI:
    """Base API wrapper for the MaveDB REST API.

    Args:
        *args (any): URL parameters as args
    Kwargs:
        **kwargs (any): URL parameters as kwargs
    """

    base_url = "https://mavedb.org/api"
    api_endpt = ""
    params = {}

    def __init__(self, *args, **kwargs):
        # Convert args to kwargs, linking arg values to their variable names.
        kwargs.update(zip(type(self).__init__.__code__.co_varnames[1:], args))
        self.params = kwargs

    @property
    def url(self):
        """Generates MaveDB REST API URL.

        Returns:
            (str): Generated URL
        """
        path = f"{urljoin(self.base_url, self.api_endpt)}"
        if not self.params:
            return path
        return path + f"?{urllib.parse.urlencode(self.params)}"


def requests_handler(method):
    """Uses method signatures to dispatch requests.

    Args:
        *args (any): *args for requests.Session methods (e.g. requests.get)
    Kwargs:
        **kwargs (any): **kwargs for requests.Session methods

    Returns:
        (requests.models.Response): Requests response from MaveDB REST API query
    """
    requests_methods = {
        "delete": requests.delete,
        "get": requests.get,
        "patch": requests.patch,
        "post": requests.post,
        "put": requests.put,
    }

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        requests_method = requests_methods[method.__name__]
        response = requests_method(self.url, *args, **kwargs)
        response.raise_for_status()
        return response

    return wrapper
