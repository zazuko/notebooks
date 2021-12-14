#!/bin/sh

set -eux

jupyter nbconvert --execute --to=html --template=./html/zazuko notebooks/zefix/zefix.ipynb
jupyter nbconvert --execute --to=html --template=./html/zazuko notebooks/animal_disease/epidemics.ipynb
jupyter nbconvert --execute --to=html --template=./html/zazuko notebooks/statistics_zurich/population.ipynb
jupyter nbconvert --execute --to=html --template=./html/zazuko notebooks/statistics_zurich/economy.ipynb
jupyter nbconvert --execute --to=html --template=./html/zazuko notebooks/statistics_zurich/real_estate.ipynb
jupyter nbconvert --execute --to=html --template=./html/zazuko notebooks/statistics_zurich/data_model.ipynb
jupyter nbconvert --execute --to=html --template=./html/zazuko notebooks/electricity_prices/electricity_prices.ipynb

mv notebooks/**/*.html html/
rsync -avr notebooks/img html/
