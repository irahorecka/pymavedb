"""
mavedb.api
~~~~~~~~~~

Suite of MaveDB API endpoints.


MAVEDB API WISHLIST
-------------------
HOW IT SHOULD FEEL...

# GET scoresets with URN as JSON
>>> mavedb.scoresets(urn="urn:mavedb:00000040-a-4").get().json()
# POST scoresets(?) with URN
>>> mavedb.scoresets(urn="urn:mavedb:00000040-a-4").post(files=file_obj)

In this form, we can add keyword arguments we'd add to requests.get()
to our method .get(), e.g. `timeout`. Same goes for post, put, delete, etc....


FEATURES DISCUSSION
-------------------
- Should we return a requests response for every call? (Simplest and most extendable)
- Or should we return a JSONified response...
    - In this form, we can move parameters to methods such as 'get'.
    E.g.,
    >>> mavedb.scoresets.get(urn="urn:mavedb:00000040-a-4")
    >>> mavedb.scoresets.get(limit=100)
"""

from mavedb.base import BaseAPI, requests_handler


class doi(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class ensembl(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class experiments(BaseAPI):
    def __init__(self, urn=""):
        super().__init__(urn=urn)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class experimentsets(BaseAPI):
    def __init__(self, urn=""):
        super().__init__(urn=urn)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class genome(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class keyword(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class pubmed(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class reference(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class refseq(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class scoresets(BaseAPI):
    def __init__(self, urn="", download=False):
        # URN and downloadable flag are included in the URL path.
        super().__init__()
        self.path.append(self.__class__.__name__)
        self.path.append(urn)
        if download is True:
            self.path.append("scores")

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class sra(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class target(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class uniprot(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class users(BaseAPI):
    def __init__(self):
        super().__init__()
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass
