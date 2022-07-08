import folium
import mapclassify
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from graphly.api_client import SparqlClient


class LindasClient(SparqlClient):
    def get_commune_centroid(self, municipality: str):
        query = """
        SELECT ?geom
        WHERE {{
            {} <http://www.opengis.net/ont/geosparql#hasGeometry> ?_geom.

            SERVICE <https://geo.ld.admin.ch/query> {{
                <https://geo.ld.admin.ch/boundaries/municipality/geometry-g1/261:2022> <http://www.opengis.net/ont/geosparql#asWKT> ?geom.
            }}
        }}
        """.format(
            municipality
        )
        df = self.send_query(query)
        df = df.set_crs(epsg=4326)
        centroid = df["geom"].iloc[0].centroid
        return [centroid.x, centroid.y]

    def get_communes(self):
        query = """
        SELECT * WHERE {
            ?municipality_id a <https://schema.ld.admin.ch/Municipality>;
                <http://schema.org/name> ?municipality.
        }
        """
        df = self.send_query(query)
        return df

    def get_commune_streets(self, municipality: str):
        query = """
        PREFIX schema: <http://schema.org/>
        PREFIX admin: <https://schema.ld.admin.ch/>
        PREFIX locn: <http://www.w3.org/ns/locn#>

        SELECT ?thoroughfare ?companies ?geom
        FROM <https://lindas.admin.ch/foj/zefix>
        FROM <https://lindas.admin.ch/territorial>
        WHERE {{
        VALUES ?muni {{ {} }}
        {{
            SELECT ?thoroughfare (COUNT(?sub) AS ?companies)
            WHERE {{
                ?sub a admin:ZefixOrganisation ;
                schema:address/locn:thoroughfare ?thoroughfare;
                admin:municipality ?muni.
            }}
            GROUP BY ?thoroughfare
            ORDER BY DESC (?companies)
        }}

        SERVICE <https://geo.ld.admin.ch/query> {{
            GRAPH <urn:bgdi:boundaries:municipalities> {{
                ?muni_swisstopo schema:about ?muni.
            }}

            GRAPH <urn:bgdi:location:streets> {{
                ?street_id a <http://www.opengis.net/ont/geosparql#Feature>;
                schema:name ?thoroughfare;
                schema:containedInPlace ?muni_swisstopo;
                <http://www.opengis.net/ont/geosparql#hasGeometry>/<http://www.opengis.net/ont/geosparql#asWKT> ?geom.
            }}
        }}
        }}
        """.format(
            municipality
        )

        df = self.send_query(query)
        df = df.set_crs(epsg=4326)

        return df


def style_function(feature, N=6, cmap=plt.get_cmap("inferno")):
    bucket = df["bucket"].get(int(feature["id"][-5:]), None)
    if bucket == 0 and df["companies"].get(int(feature["id"][-5:]), None) == 0:
        bucket = None
    return {
        "fillOpacity": 0.6,
        "weight": 3,
        "opacity": 1,
        "fillColor": "303030"
        if bucket is None
        else mcolors.rgb2hex(cmap((bucket + 1) / N)),
        "color": "303030"
        if bucket is None
        else mcolors.rgb2hex(cmap((bucket + 1) / N)),
    }
