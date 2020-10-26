from SPARQLWrapper import SPARQLWrapper, SPARQLWrapper2, JSON, POST

sparql = SPARQLWrapper2("https://lindas.admin.ch/query")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX qb: <http://purl.org/linked-data/cube#>

    SELECT ?dataset ?label (COUNT(DISTINCT ?observation) AS ?observations)
    FROM <https://linked.opendata.swiss/graph/zh/statistics>
    WHERE{
        ?observation a qb:Observation;
            qb:dataSet ?dataset.
        ?dataset rdfs:label ?label.
    }
    GROUP BY ?dataset ?label
    ORDER BY DESC(?observations)
""")
sparql.setMethod(POST)
sparql.setReturnFormat(JSON)
results = sparql.query().bindings