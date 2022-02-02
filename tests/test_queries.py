import json
from typing import TypedDict

import pytest
from graphly.api_client import SparqlClient

with open("tests/queries.json") as f:
    testcases = json.load(f)


class EndpointTest(TypedDict):

    endpoint: str
    prefixes: dict[str, str]
    queries: list[str]


class Test_ssz_queries:
    @classmethod
    def setup_class(cls):

        cls.endpoint = "https://ld.stadt-zuerich.ch/query"
        cls.client = SparqlClient(cls.endpoint, timeout=30)
        cls.client.add_prefixes(testcases[cls.endpoint]["prefixes"])

    def test_endpoint(self):

        query = "SELECT * WHERE {?s ?p ?o} LIMIT 3"
        df = self.client.send_query(query, timeout=None)
        assert df.shape[0] == 3

    test_data = testcases["https://ld.stadt-zuerich.ch/query"]["queries"]

    @pytest.mark.parametrize("query", test_data)
    def test_queries(self, query):

        df = self.client.send_query(query)
        assert df.shape[0] > 0


@pytest.mark.skip(reason="Skip lindas")
class Test_lindas_queries:
    @classmethod
    def setup_class(cls):

        cls.endpoint = "https://lindas.admin.ch/query"
        cls.client = SparqlClient(cls.endpoint, timeout=30)
        cls.client.add_prefixes(testcases[cls.endpoint]["prefixes"])

    def test_endpoint(self):

        query = "SELECT * WHERE {?s ?p ?o} LIMIT 3"
        df = self.client.send_query(query, timeout=None)
        assert df.shape[0] == 3

    test_data = testcases["https://lindas.admin.ch/query"]["queries"]

    @pytest.mark.parametrize("query", test_data)
    def test_queries(self, query):

        df = self.client.send_query(query)
        assert df.shape[0] > 0


@pytest.mark.skip(reason="Skip geoadmin")
class Test_geoadmin_queries:
    @classmethod
    def setup_class(cls):

        cls.endpoint = "https://ld.geo.admin.ch/query"
        cls.client = SparqlClient(cls.endpoint, timeout=30)
        cls.client.add_prefixes(testcases[cls.endpoint]["prefixes"])

    def test_endpoint(self):

        query = "SELECT * WHERE {?s ?p ?o} LIMIT 3"
        df = self.client.send_query(query, timeout=None)
        assert df.shape[0] == 3

    test_data = testcases["https://ld.geo.admin.ch/query"]["queries"]

    @pytest.mark.parametrize("query", test_data)
    def test_queries(self, query):

        df = self.client.send_query(query)
        assert df.shape[0] > 0


class Test_wikidata_queries:
    @classmethod
    def setup_class(cls):

        cls.endpoint = "https://query.wikidata.org/sparql"
        cls.client = SparqlClient(cls.endpoint, timeout=30)
        cls.client.add_prefixes(testcases[cls.endpoint]["prefixes"])

    test_data = testcases["https://query.wikidata.org/sparql"]["queries"]

    @pytest.mark.parametrize("query", test_data)
    def test_queries(self, query):

        df = self.client.send_query(query)
        assert df.shape[0] > 0
