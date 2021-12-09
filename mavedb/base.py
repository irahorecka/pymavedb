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
        auth_token (str): Authorization token for MaveDB. Required for
                          requests requiring authorized credentials
    Kwargs:
        **kwargs (any): URL parameters as kwargs
    """

    base_url = "https://mavedb.org/api"

    def __init__(self, auth_token, **kwargs):
        self.auth_token = auth_token
        self.path = []
        self.params = kwargs

    @property
    def url(self):
        """Generates MaveDB REST API URL.

        Returns:
            (str): Generated URL
        """
        # By default, urllib.parse.quote() function is intended for quoting the path section of a URL.
        url_ = urljoin(self.base_url, urllib.parse.quote(urljoin(*self.path)))
        if not any(self.params.values()):
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

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        requests_methods = {
            "delete": functools.partial(requests.delete, headers={"Authorization": self.auth_token}),
            "get": requests.get,
            "patch": functools.partial(requests.patch, headers={"Authorization": self.auth_token}),
            "post": functools.partial(requests.post, headers={"Authorization": self.auth_token}),
            "put": functools.partial(requests.put, headers={"Authorization": self.auth_token}),
        }
        requests_method = requests_methods[method.__name__]
        response = requests_method(self.url, *args, **kwargs)
        response.raise_for_status()
        return response

    return wrapper
