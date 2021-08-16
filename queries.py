queries = [
    {
        "endpoint": "https://ld.integ.stadt-zuerich.ch/query/",
        "prefixes": {
            "schema": "<http://schema.org/>",
            "cube": "<https://cube.link/>",
            "property": "<https://ld.stadt-zuerich.ch/statistics/property/>",
            "measure": "<https://ld.stadt-zuerich.ch/statistics/measure/>",
            "skos": "<http://www.w3.org/2004/02/skos/core#>",
            "ssz": "<https://ld.stadt-zuerich.ch/statistics/>",
        },
        "queries": [
            """
SELECT ?time ?place ?rooms ?price
FROM <https://lindas.admin.ch/stadtzuerich/stat>
WHERE {
  ssz:QMP-EIG-HAA-OBJ-ZIM a cube:Cube;
             cube:observationSet/cube:observation ?observation.
  ?observation property:TIME ?time ;
                       property:RAUM ?place_uri;
                       property:ZIM/schema:name ?rooms;
                       measure:QMP ?price .
  ?place_uri skos:inScheme <https://ld.stadt-zuerich.ch/statistics/scheme/Kreis> ;
         schema:name ?place .
  FILTER regex(str(?place),"ab|Stadtgebiet vor")
  FILTER (?price > 0)
}
ORDER BY ?time
""",
            """
SELECT *
FROM <https://lindas.admin.ch/stadtzuerich/stat>
WHERE{
    {
      SELECT ?time (SUM(?pop_count) AS ?pop)
      WHERE {
        ssz:BEW a cube:Cube;
                   cube:observationSet/cube:observation ?obs_bew.
        ?obs_bew property:TIME ?time ;
                 property:RAUM ?place_uri_pop;
                 measure:BEW ?pop_count .

        ?place_uri_pop skos:inScheme <https://ld.stadt-zuerich.ch/statistics/scheme/Kreis> ;
                   schema:name ?place_pop .

        FILTER regex(str(?place_pop),"ab|Stadtgebiet vor")
      }
      GROUP BY ?time
    }
    {
      SELECT ?time (SUM(?apt_count) AS ?apts)
      WHERE {
        ssz:WHG a cube:Cube;
                   cube:observationSet/cube:observation ?obs_apt.
        ?obs_apt property:TIME ?time ;
                 property:RAUM ?place_uri_apt;
                 measure:WHG ?apt_count .

        ?place_uri_apt skos:inScheme <https://ld.stadt-zuerich.ch/statistics/scheme/Kreis> ;
                   schema:name ?place .

        FILTER regex(str(?place),"ab|Stadtgebiet vor")
      }
      GROUP BY ?time
    }
}
ORDER BY ?time
""",
            """
SELECT ?time ?rooms (SUM(?count) AS ?apts)
FROM <https://lindas.admin.ch/stadtzuerich/stat>
WHERE {
  ssz:WHG-ZIM a cube:Cube;
             cube:observationSet/cube:observation ?obs.
  ?obs property:TIME ?time ;
           property:RAUM ?place_uri;
           property:ZIM/schema:name ?rooms ;
           measure:WHG ?count .

  ?place_uri skos:inScheme <https://ld.stadt-zuerich.ch/statistics/scheme/Kreis> ;
             schema:name ?place .

  FILTER regex(str(?place),"ab|Stadtgebiet vor")
  FILTER (?time >= "1977-01-01"^^xsd:time)
}
GROUP BY ?time ?rooms
ORDER BY ?time ?rooms
""",
        ],
    }
]
