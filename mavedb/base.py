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
    path = ""
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
        # By default, urllib.parse.quote() function is intended for quoting the path section of a URL.
        url_ = urljoin(self.base_url, urllib.parse.quote(self.path))
        if not self.params:
            return url_
        # Use urllib.parse.quote() to quote parameters passed to urllib.parse.urlencode().
        return url_ + "?" + urllib.parse.urlencode(self.params, quote_via=urllib.parse.quote)


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
