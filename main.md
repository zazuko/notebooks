# Statistik Stadt Zurich

Available datasets are:
* [Population](http://localhost:8888/notebooks/population.ipynb)
* [Real estate](http://localhost:8888/notebooks/real_estate.ipynb)
* [Economy](http://localhost:8888/notebooks/economy.ipynb)


* [Graph exploration I](http://localhost:8888/notebooks/exploratory_queries.ipynb)
* [Graph exploration II](http://localhost:8888/notebooks/exploring_ssz_graph.ipynb)


## Datasets

### Population
* BEW: Wirtschaftliche Wohnbevölkerung
* BEW-ALT: Wirtschaftliche Wohnbevölkerung nach Alter
* BEW-ALT-HEL: Wirtschaftliche Wohnbevölkerung nach Alter, Heimatland
* BEW-ALT-HEL-SEX: Wirtschaftliche Wohnbevölkerung nach Alter, Heimatland, Geschlecht
* BEW-ALT-SEX: Wirtschaftliche Wohnbevölkerung nach Alter, Geschlecht
* BEW-HEL: Wirtschaftliche Wohnbevölkerung nach Heimatland
* BEW-HEL-SEX: Wirtschaftliche Wohnbevölkerung nach Heimatland, Geschlecht
* BEW-SEX: Wirtschaftliche Wohnbevölkerung nach Geschlecht
* ANT-GGH-HEL: Anteil nach Grundgesamtheit, Heimatland

Dimensions: Population, Age, Gender, Origin, Time, Place

### Real estate
* APZ: Appartementzimmer
* WHA: Wohnungen (ohne Appartements)
* WHA-ZIM: Wohnungen (ohne Appartements) nach Zimmerzahl einer Wohnung
* WHG: Statistische Wohnungen
* WHG-ZIM: Statistische Wohnungen nach Zimmerzahl einer Wohnung
* ZIM: Zimmer
* ZIM-WHA: Zimmer nach Wohnungsart
* QMP-EIG-HAA-OBJ-ZIM: Quadratmeterpreis nach Eigentümerart, Handänderungsart, Objektart, Zimmerzahl einer Wohnung

 Dimensions: Appartments, Price, Time, Place

### Deaths
* GES-ALT-SEX: Sterbefälle (wirtschaftlich) nach Alter, Geschlecht
* GES-ALT-SEX-TOU: Sterbefälle (wirtschaftlich) nach Alter, Geschlecht, Todesursachen
* GES-SEX: Sterbefälle (wirtschaftlich) nach Geschlecht
* GES-SEX-TOU: Sterbefälle (wirtschaftlich) nach Geschlecht, Todesursachen

Dimensions: Deaths, Age, Gender, Death cause, Time

### Workplaces
* AST-BEW-BTA: Arbeitsstätten nach Bewilligung, Betriebsart -> number of cafeterias over time, per district
* AST-BTA: Arbeitsstätten nach Betriebsart -> number of cafeterias/restaurants over time, districts

* BES-BTA: Beschäftigte nach Betriebsart
* BES-BTA-SEX: Beschäftigte nach Betriebsart, Geschlecht


### Animals
* TIA-BTA: Tierarten nach Betriebsart
* TIA-BTA-TIG: Tierarten nach Betriebsart, Tiergattung
* TII-BTA: Tierindividuen nach Betriebsart
* TII-BTA-TIG: Tierindividuen nach Betriebsart, Tiergattung

 TODO: analyse dimensions




## Skipped:

### Zoo, Horte
* WRT-BTA-EAP: Wert nach Betriebsart, Erfolgsrechnung -> Income statement
* ZUS-BTA: Zuschauer/innen, Besucher/innen nach Betriebsart
* ZUS-BTA-HEL: Zuschauer/innen, Besucher/innen nach Betriebsart, Heimatland
* ZUS-BTA-SEX: Zuschauer/innen, Besucher/innen nach Betriebsart, Geschlecht
* ZUS-BTA-ZSA: Zuschauer/innen, Besucher/innen nach Betriebsart, Zuschauer- bzw. Besucherart