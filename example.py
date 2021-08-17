import json
import re

cell = 'query = """\nSELECT ?time ?place ?rooms ?price\nFROM <https://lindas.admin.ch/stadtzuerich/stat>\nWHERE {\n  ssz:QMP-EIG-HAA-OBJ-ZIM a cube:Cube;\n             cube:observationSet/cube:observation ?observation.   \n  ?observation property:TIME ?time ;\n                       property:RAUM ?place_uri;\n                       property:ZIM/schema:name ?rooms;\n                       measure:QMP ?price .\n  ?place_uri skos:inScheme <https://ld.stadt-zuerich.ch/statistics/scheme/Kreis> ;\n         schema:name ?place .\n  FILTER regex(str(?place),"ab|Stadtgebiet vor")\n  FILTER (?price > 0)\n}\nORDER BY ?time\n"""\n\ndf = sparql.send_query(query)\ndf.head()'

query = re.search(r'query = """(.*?)"""', cell, flags=re.DOTALL)
print(if query)
