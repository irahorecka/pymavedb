"""
mavedb.api
~~~~~~~~~~

Suite of MaveDB API endpoints.
"""

import functools

from mavedb.base import BaseAPI, requests_handler


class doi(BaseAPI):
    """/doi - Queries the Digital Object Identifiers (DOI) list."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class ensembl(BaseAPI):
    """/ensembl - Queries identifiers in the Ensembl database."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class experiments(BaseAPI):
    """/experiments - Queries Mave experiments."""

    def __init__(self, auth_token, urn=""):
        super().__init__(auth_token, urn=urn)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class experimentsets(BaseAPI):
    """/experimentsets - Queries Mave experimentsets.
    Experimentsets are the parent category of experiments.
    """

    def __init__(self, auth_token, urn=""):
        super().__init__(auth_token, urn=urn)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class genome(BaseAPI):
    """/genome - Queries identifiers in the GenomeAssembly database."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class keyword(BaseAPI):
    """/keyword - Queries Mave keywords."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class pubmed(BaseAPI):
    """/pubmed - Queries identifiers in the PubMed database."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class reference(BaseAPI):
    """/reference - Queries identifiers in the Reference Genome list."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class refseq(BaseAPI):
    """/refseq - Queries identifiers in the Refseq Identifier list."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class scoresets(BaseAPI):
    """/scoresets - Queries the Mave Score Set list."""

    def __init__(self, auth_token, urn="", download=False):
        super().__init__(auth_token)
        # URN and downloadable flag are included in the URL path.
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
    """/sra - Queries the Sequence Read Archive (SRA) identifier list."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class target(BaseAPI):
    """/target - Queries the Mave Target Gene list."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class uniprot(BaseAPI):
    """/uniprot - Queries identifiers in the UniProt database."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class users(BaseAPI):
    """/users - Queries the Mave User list."""

    def __init__(self, auth_token):
        super().__init__(auth_token)
        self.path.append(self.__class__.__name__)

    @requests_handler
    def get(self, *args, **kwargs):
        pass

    @requests_handler
    def post(self, *args, **kwargs):
        pass


class MaveDB:
    """Public API class to interface with the Mave Database (MaveDB).

    Kwargs:
        auth_token (str): Authorization token for MaveDB. Required for
                          requests requiring authorized credentials
    """

    def __init__(self, auth_token=None):
        self.doi = functools.partial(doi, auth_token)
        self.ensembl = functools.partial(ensembl, auth_token)
        self.experiments = functools.partial(experiments, auth_token)
        self.experimentsets = functools.partial(experimentsets, auth_token)
        self.genome = functools.partial(genome, auth_token)
        self.keyword = functools.partial(keyword, auth_token)
        self.pubmed = functools.partial(pubmed, auth_token)
        self.reference = functools.partial(reference, auth_token)
        self.refseq = functools.partial(refseq, auth_token)
        self.scoresets = functools.partial(scoresets, auth_token)
        self.sra = functools.partial(sra, auth_token)
        self.target = functools.partial(target, auth_token)
        self.uniprot = functools.partial(uniprot, auth_token)
        self.users = functools.partial(users, auth_token)
