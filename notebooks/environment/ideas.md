## Datasets overview:

### 1. Bathing water quality

- cube: https://environment.ld.admin.ch/foen/ubd0104/3/
- dimensions:
    * measurement station
    * bacteria (Enterokokken/E.coli)
    * time
- ideas:
    * heatmap: measurement stations + concentration [exists here](https://www.bafu.admin.ch/bafu/de/home/themen/wasser/fachinformationen/zustand-der-gewaesser/zustand-der-fliessgewaesser/wasserqualitaet-der-fliessgewaesser/badegewaesserqualitaet.html)
    * time series: concentration of one bacteria, in one station
    * distribution: for each bacteria, all values aggregated

### 2. Heavy metal concentration in the soil
- cube: https://environment.ld.admin.ch/foen/ubd0066/4/
- dimensions:
    * measurement station (+land use)
    * heavy metal (6 metals)
    * time

ideas: see `heavy_metal.ipynb`


### 3. Noise pollution
- cube: https://environment.ld.admin.ch/foen/ubd0037/3/
- dimensions:
    * traffic type (rails/highways/aerial/total)
    * assesment (ok/not ok)
    * period (day/night)
    * region type (city center/around city/outside of city)
    * metric (aparments/ppl/buildings)

Exposition of ppl/flats/buildings to noise.
- query: https://s.zazuko.com/4BYKK6

All plots time series!
Ideas:
- trends in total noise (%ppl exposed to noise over time)
- noise composition over time
- repeat for day and night
- aggregate for region types OR repeat for each region type

- noise exposition of buildings vs ppl
- noise exposition in rural and central areas

Q: do we see the same in economic data?





Alternative ideas:
- [divorce rates](https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken/tabellen.html?dyn_prodima=900010&dyn_publishingyearend=2022&dyn_title=scheidungen&dyn_pageIndex=1)
- disease rates
- population and economic trends
- tax rates across communes




