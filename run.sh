#!/bin/sh

set -eux

jupyter nbconvert --to=html --template=./html/zazuko notebooks/**/*.ipynb
mv notebooks/**/*.html html/
rsync -avr notebooks/img html/img
