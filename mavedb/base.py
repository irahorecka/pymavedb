import functools
import urllib
from posixpath import join as urljoin

import requests


class BaseAPI:
    """Base wrapper for individual AC Transit APIs."""

    base_url = "https://mavedb.org/api"
    api_endpt = ""
    params = {}

    def __init__(self, **kwargs):
        self.params = kwargs

    @property
    def url(self):
        path = f"{urljoin(self.base_url, self.api_endpt)}"
        if not self.params:
            return path
        return path + f"?{urllib.parse.urlencode(self.params)}"


def requests_handler(func):
    """Decorator for using method signatures to validate and make API calls."""
    requests_methods = {
        "delete": requests.delete,
        "get": requests.get,
        "patch": requests.patch,
        "post": requests.post,
        "put": requests.put,
    }

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Set requests instance
        requests_method = requests_methods[func.__name__]
        response = requests_method(self.url, *args, **kwargs)
        response.raise_for_status()
        return response

    return wrapper
