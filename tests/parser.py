import json
import os
import pprint
import re
from enum import Enum
from typing import Literal, TypedDict, Union

pp = pprint.PrettyPrinter(indent=4)


def is_notebook(file: str) -> bool:
    return file.endswith(".ipynb") and not file.endswith("checkpoint.ipynb")


def get_notebooks_path(root: str) -> list[str]:

    return [
        os.path.join(path, file)
        for path, _, files in os.walk(root)
        for file in files
        if is_notebook(file)
    ]


class JupyterCell(TypedDict):

    cell_type: Union[Literal["code"], Literal["markdown"]]
    metadata: dict
    source: str


class KernelSpec(TypedDict):

    display_name: str
    language: Union[Literal["python"], Literal["sparql"]]
    name: str


class JupyterMetadata(TypedDict):

    kernelspec: KernelSpec
    language_info: dict
    title: str


class JupyterNotebook(TypedDict):

    cells: list[JupyterCell]
    metadata: JupyterMetadata
    nbformat: int
    nbformat_minor: int


class Kernels(Enum):

    Python = "python"
    Sparql = "sparql"


class EndpointTest(TypedDict):

    prefixes: dict[str, str]
    queries: list[str]


def get_testcases_from_sparql_cells(
    cells: list[JupyterCell],
) -> dict[str, EndpointTest]:

    testcases = {}
    queries = []

    for c in cells:

        if "%endpoint" in c:
            if queries and "client" in locals():
                testcases[client]: EndpointTest = {"queries": queries, "prefixes": []}
            client = re.search(r"%endpoint (.*?)\n", c).group(1)
            queries = []
        else:
            queries.append(c)

    if queries and "client" in locals():
        testcases[client]: EndpointTest = {"queries": queries, "prefixes": []}

    return testcases


def get_testcases_from_python_cells(
    cells: list[JupyterCell],
) -> dict[str, EndpointTest]:

    testcases = dict()
    alias2endpoint = dict()

    for cell in cells:

        if "SparqlClient(" in cell:

            endpoints = re.findall(r'SparqlClient\("(.*?)"\)', cell)
            aliases = re.findall(r"(.*?) = SparqlClient\(", cell)

            for alias, endpoint in zip(aliases, endpoints):

                prefix_candidate = re.search(
                    r"{}.add_prefixes\((.*?)\)".format(alias), cell, flags=re.DOTALL
                )
                if prefix_candidate:

                    prefixes = re.sub(
                        r"\s+", "", prefix_candidate.group(1), flags=re.UNICODE
                    )

                    if prefixes[-2] == ",":
                        prefixes = prefixes[:-2] + prefixes[-1]

                    prefixes = json.loads(prefixes)

                else:
                    prefixes = dict()

                alias2endpoint[alias] = endpoint
                testcases[endpoint]: EndpointTest = {
                    "queries": [],
                    "prefixes": prefixes,
                }

        if 'query = """' in cell:
            query = re.search(r'query = """(.*?)"""', cell, flags=re.DOTALL).group(1)
            if not re.match(r'query = """(.*?)""".format', cell, flags=re.DOTALL):
                alias = re.search(r"= (.*?).send_query", cell).group(1)
                testcases[alias2endpoint[alias]]["queries"].append(query)

    return testcases


def parse_notebook(notebook: JupyterNotebook) -> dict[str, EndpointTest]:

    cells = [c["source"] for c in notebook["cells"] if c["cell_type"] == "code"]
    cells = ["".join(c) for c in cells]

    if notebook["metadata"]["kernelspec"]["language"] == Kernels.Python.value:
        testcases = get_testcases_from_python_cells(cells)

    elif notebook["metadata"]["kernelspec"]["language"] == Kernels.Sparql.value:
        testcases = get_testcases_from_sparql_cells(cells)

    else:
        raise ValueError(
            "{} kernel is not supported".format(
                notebook["metadata"]["kernelspec"]["language"]
            )
        )

    return testcases


if __name__ == "__main__":

    testcases = {}
    for path in get_notebooks_path("notebooks"):

        with open(path) as f:
            notebook_data = json.load(f)

        curr_testcase = parse_notebook(notebook_data)

        for endpoint, params in curr_testcase.items():

            if endpoint not in testcases:
                testcases[endpoint] = params
            else:
                testcases[endpoint]["queries"] += params["queries"]
                testcases[endpoint]["prefixes"] |= params["prefixes"]

    with open("tests/queries.json", "w") as fp:
        json.dump(testcases, fp)
