import folium
import mapclassify
import matplotlib.pyplot as plt
from graphly.api_client import SparqlClient


class LindasClient(SparqlClient):

    client = SparqlClient("https://geo.ld.admin.ch/query")
