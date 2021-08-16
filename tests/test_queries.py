import json
from typing import Literal, TypedDict, Union

import pytest
from graphly.api_client import SparqlClient
from queries import queries


class EndpointTest(TypedDict):

    endpoint: str
    prefixes: dict[str, str]
    queries: list[str]


testcases = json.loads("queries.json")


class Test_sparql_queries:
    @classmethod
    def setup_class(cls):

        cls.client = SparqlClient(
            "https://ld.integ.stadt-zuerich.ch/query/", timeout=30
        )
        cls.client.add_prefixes(
            {
                "schema": "<http://schema.org/>",
                "cube": "<https://cube.link/>",
                "property": "<https://ld.stadt-zuerich.ch/statistics/property/>",
                "measure": "<https://ld.stadt-zuerich.ch/statistics/measure/>",
                "skos": "<http://www.w3.org/2004/02/skos/core#>",
                "ssz": "<https://ld.stadt-zuerich.ch/statistics/>",
            }
        )
        cls.queries = queries[0]["queries"]

    test_data = [
        ({"value": "whatever"}, "type"),
        ({"type": "whatever"}, "value"),
        ({"a": "b"}, "type"),
    ]

    @pytest.mark.parametrize("coordinates_body, missing_field", test_data)
    def test_queries(self, query):

        df = self.client.send_query(query)

        assert df.shape[0] > 0
