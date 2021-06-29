#!/bin/sh

set -eux

cp -r html/zazuko venv/share/jupyter/nbconvert/templates/
jupyter nbconvert --to=html --template=zazuko notebooks/*.ipynb
mv notebooks/*.html html/
rsync -avr notebooks/img/ html/img
