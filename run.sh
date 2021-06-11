
jupyter nbconvert --to=html notebooks/*.ipynb
mv notebooks/*.html html/
cp -R notebooks/img html/img
