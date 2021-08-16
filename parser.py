import json
import os
import pprint
import re
from enum import Enum
from typing import Literal, TypedDict, Union

from graphly.api_client import SparqlClient

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


def parse_notebook(notebook: JupyterNotebook) -> tuple[list[str], list[str]]:

    cells = [c["source"] for c in notebook["cells"] if c["cell_type"] == "code"]
    cells = ["".join(c) for c in cells]

    if notebook["metadata"]["kernelspec"]["language"] == Kernels.Python.value:
        clients = [c for c in cells if "SparqlClient(" in c]
        queries = [c for c in cells if c.startswith('query = """')]

    elif notebook["metadata"]["kernelspec"]["language"] == Kernels.Sparql.value:
        clients = [
            re.search(r"%endpoint (.*?)\n", c).group(1)
            for c in cells
            if "%endpoint" in c
        ]
        queries = [c for c in cells if "%endpoint" not in c]

    else:
        raise ValueError(
            "{} kernel is not supported".format(
                notebook["metadata"]["kernelspec"]["language"]
            )
        )

    return clients, queries


# print(cells[-1])

notebooks = get_notebooks_path("notebooks")

path = notebooks[3]


with open(path) as f:
    data = json.load(f)

clients, queries = parse_notebook(data)
# pp.pprint(clients[0])
print(repr(queries[0]))

# endpoint = clients[0]
# sparql = SparqlClient(endpoint)
# df = sparql.send_query(queries[0])
# print(df.shape[0] > 0)

print(path)
with open("queries.py", "w+") as file:

    for client in clients:
        file.write(client + "\n\n")

    for query in queries:
        file.write(query + "\n\n")


# TODO: add special treatment for SPARQL notebooks
