from graphly.api_client import SparqlClient

ENDPOINT = "https://ld.stadt-zuerich.ch/query/"

client = SparqlClient(ENDPOINT)

client.add_prefixes({
    "schema": "<http://schema.org/>",
    "cube": "<https://cube.link/>",
    "ssz": "<https://ld.stadt-zuerich.ch/statistics/property/>"
})

query = """
SELECT ?time ?place ?sex ?alt ?tou ?ges

FROM <https://lindas.admin.ch/stadtzuerich/stat>
WHERE {
  <https://ld.stadt-zuerich.ch/statistics/GES-ALT-SEX-TOU> a cube:Cube;
             cube:observationSet/cube:observation ?observation.

        ?observation ?p ?measure ;
                 ssz:RAUM ?raum ;
                 ssz:TIME ?time ;
                 <https://ld.stadt-zuerich.ch/statistics/measure/GES> ?ges ;
                 ssz:SEX ?sex ;
                 ssz:TOU ?tou ;
                 ssz:ALT ?alt .

    ?raum schema:name ?place .

    # ISSUE:
    # ?sex schema:name ?gender .

    #FILTER(regex(str(?p), "https://ld.stadt-zuerich.ch/statistics/measure/"))
    #FILTER(?p NOT IN (<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>, <http://www.w3.org/2004/02/skos/core#notation>, <https://ld.stadt-zuerich.ch/statistics/attribute/KORREKTUR>, <https://cube.link/observedBy>))

}
LIMIT 15
"""
res = client.send_query(query)
print(res.head())
#for cube in cubes["s"].tolist():
#    print(cube)

#prefix = {"A": 1, "B": 2, "C": 3}
#res = '\n'.join("PREFIX %s" % ': '.join(map(str, x)) for x in prefix.items()) + "\n"
#print(res + query)