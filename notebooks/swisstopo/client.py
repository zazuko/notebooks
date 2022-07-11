from graphly.api_client import SparqlClient


class LindasClient(SparqlClient):
    def get_commune_centroid(self, municipality: str):

        query = """
        SELECT ?geom
        WHERE {{
            <{}> <http://www.opengis.net/ont/geosparql#hasGeometry> ?_geom.

            SERVICE <https://geo.ld.admin.ch/query> {{
                ?_geom <http://www.opengis.net/ont/geosparql#asWKT> ?geom.
            }}
        }}
        """.format(
            municipality
        )
        df = self.send_query(query)
        df = df.set_crs(epsg=4326)
        centroid = df["geom"].iloc[0].centroid
        return [centroid.y, centroid.x]

    def get_communes(self):
        query = """
        SELECT * WHERE {
            ?municipality_id a <https://schema.ld.admin.ch/Municipality>;
                <http://schema.org/name> ?municipality.
        }
        ORDER BY ?municipality
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
        VALUES ?muni {{ <{}> }}
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
