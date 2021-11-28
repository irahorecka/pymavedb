"""
MAVEDB API WISHLIST
-------------------
HOW IT SHOULD FEEL...

# GET scoresets with URN as JSON
>>> mavedb.scoresets(urn="urn:mavedb:00000040-a-4").get().json()
# POST scoresets(?) with URN
>>> mavedb.scoresets(urn="urn:mavedb:00000040-a-4").post(files=file_obj)

In this form, we can add keyword arguments to .get() that we'd normally
add to requests.get, e.g. `timeout`. Same goes for post, put, delete, etc....


FEATURES DISCUSSION
-------------------
- Should we return a requests response for every call? (Simplest)
- Or should we return a JSONified response...
    - In this form, we can move parameters to methods such as 'get'.
    E.g.,
    >>> mavedb.scoresets.get(urn="urn:mavedb:00000040-a-4")
    >>> mavedb.scoresets.get(limit=100)
"""

from posixpath import join as urljoin

from base import BaseAPI, requests_handler


class doi(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class ensembl(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class experiments(BaseAPI):
    def __init__(self, urn=""):
        self.api_endpt = self.__class__.__name__
        super().__init__(urn=urn)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class experimentsets(BaseAPI):
    def __init__(self, urn=""):
        self.api_endpt = self.__class__.__name__
        super().__init__(urn=urn)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class genome(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class keyword(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class pubmed(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class reference(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class refseq(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class scoresets(BaseAPI):
    def __init__(self, urn="", download=False):
        # URN and downloadable flag are API endpoints.
        self.api_endpt = urljoin(self.__class__.__name__, urn)
        if download is True:
            self.api_endpt = urljoin(self.api_endpt, "scores")
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class sra(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class target(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class uniprot(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class users(BaseAPI):
    def __init__(self):
        self.api_endpt = self.__class__.__name__
        super().__init__()

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass
