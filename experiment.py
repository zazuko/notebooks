from graphly.api_client import SparqlClient

ENDPOINT = "https://ld.zazuko.com/query/"

client = SparqlClient(ENDPOINT)

client.add_prefixes({
    "schema": "<http://schema.org/>",
    "cube": "<https://cube.link/>",
    "ssz": "<https://ld.stadt-zuerich.ch/statistics/property/>"
})

query = """
SELECT ?time ?place ?count
FROM <https://lindas.admin.ch/stadtzuerich/stat>
WHERE {
  <https://ld.stadt-zuerich.ch/statistics/BEW> a cube:Cube;
             cube:observationSet/cube:observation ?observation.

  ?observation ssz:RAUM ?place_uri ;
                       ssz:TIME ?time ;
                       <https://ld.stadt-zuerich.ch/statistics/measure/BEW> ?count .
  ?place_uri <http://www.w3.org/2004/02/skos/core#inScheme> <https://ld.stadt-zuerich.ch/statistics/scheme/Kreis> ;
         <http://schema.org/name> ?place .
  FILTER regex(str(?place),"ab|Stadtgebiet vor")
}
ORDER BY ?time
"""
res = client.send_query(query)
print(res.head())