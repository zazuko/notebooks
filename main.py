import os

import pandas as pd
from dotenv import load_dotenv
from graphly.api_client import SparqlClient
from sqlalchemy import create_engine

int = SparqlClient("https://int.lindas.admin.ch/query")
apps = SparqlClient("https://trifid-lindas.apps.cluster.ldbar.ch/query")

load_dotenv()
engine = create_engine(
    "postgresql://{}:{}@{}/{}".format(
        os.getenv("SQL_USER"),
        os.getenv("SQL_PASSWORD"),
        os.getenv("SQL_HOST"),
        os.getenv("DBNAME"),
    ),
    echo=False,
)

query_int = """
PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cube: <https://cube.link/>

SELECT ?obs ?netzbetreiber ?gemeindeNummer ?gemeindeName ?kategorieName ?total ?energie ?abgaben ?netznutzung ?foerderabgaben

FROM <https://lindas.admin.ch/elcom/electricityprice>
FROM <https://lindas.admin.ch/territorial>

WHERE {
  {
  SELECT ?operator ?netzbetreiber ?netzbetreiberStrasse ?netzbetreiberPlz ?netzbetreiberOrt {
  ?operator a schema:Organization ;
           schema:name ?netzbetreiber ;
  }
  }

   <https://energy.ld.admin.ch/elcom/electricityprice> a cube:Cube ;
       cube:observationSet/cube:observation ?obs .

   ?obs <https://energy.ld.admin.ch/elcom/electricityprice/dimension/period> "2023"^^xsd:gYear ;
        <https://energy.ld.admin.ch/elcom/electricityprice/dimension/municipality> ?municipality;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/category> ?category ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/product> <https://energy.ld.admin.ch/elcom/electricityprice/product/standard> ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/total> ?total ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/energy> ?energie ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/charge> ?abgaben ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/gridusage> ?netznutzung ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/aidfee> ?foerderabgaben ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/operator> ?operator .


  ?municipality schema:name ?gemeindeName ;
                schema:identifier ?gemeindeNummer ;
                schema:containedInPlace ?canton .

  ?canton a <https://schema.ld.admin.ch/Canton> ;
          schema:alternateName ?kanton .

  ?category schema:name ?kategorieName .

} ORDER BY ?gemeindeNummer ?kategorieName
"""

query_apps = """
PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cube: <https://cube.link/>

SELECT ?obs ?netzbetreiber ?gemeindeNummer ?gemeindeName ?kategorieName ?total ?energie ?abgaben ?netznutzung ?foerderabgaben

FROM <https://lindas.admin.ch/elcom/electricityprice>
FROM <https://lindas.admin.ch/territorial>

WHERE {
  {
  SELECT ?operator ?netzbetreiber ?netzbetreiberStrasse ?netzbetreiberPlz ?netzbetreiberOrt {
  ?operator a schema:Organization ;
           schema:name ?netzbetreiber ;
  }
  }

   <https://energy.ld.admin.ch/elcom/electricityprice> a cube:Cube ;
       cube:observationSet/cube:observation ?obs .

   ?obs <https://energy.ld.admin.ch/elcom/electricityprice/dimension/period> "2023"^^xsd:gYear ;
        <https://energy.ld.admin.ch/elcom/electricityprice/dimension/municipality> ?municipality;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/category> ?category ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/product> <https://energy.ld.admin.ch/elcom/electricityprice/product/standard> ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/total> ?total ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/energy> ?energie ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/charge> ?abgaben ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/gridusage> ?netznutzung ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/aidfee> ?foerderabgaben ;
         <https://energy.ld.admin.ch/elcom/electricityprice/dimension/operator> ?operator .


  ?municipality schema:name ?gemeindeName ;
                schema:identifier ?gemeindeNummer ;
                schema:containedInPlace ?canton .

  ?canton a <https://schema.ld.admin.ch/Canton> ;
          schema:alternateName ?kanton .

  ?category schema:name ?kategorieName .

} ORDER BY ?gemeindeNummer ?kategorieName
"""


df_int = int.send_query(query_int)
df_apps = int.send_query(query_apps)


df_int.to_sql("Int", engine, if_exists="replace", index_label="obs", index=False)
df_apps.to_sql("Apps", engine, if_exists="replace", index_label="obs", index=False)
