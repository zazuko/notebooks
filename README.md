# Linked Data by Zazuko

[Zazuko](http://zazuko.com/) collects and publishes data from all areas of life. That includes demographics, economy, environment and politics. Corresponding datasets are published as [Linked Data](https://en.wikipedia.org/wiki/Linked_data).

These tutorials show **how to work with Linked Data**. They will guide you to working with SPAQRL directly in python. We recommend them to people who would like to:

* Learn to query Linked Data
* Explore datasets about Switzerland

## Install
### Locally
To setup the project locally after you have cloned this repository:
* ```python3 -m venv venv``` create virtual environment
* ```source venv/bin/activate``` to activate venv on Linux or  ```venv\Scripts\activate.bat``` to activate venv on Windows
* ```pip install -r requirements.txt``` install dependencies
* ```python -m ipykernel install --user --name=zazuko``` add python kernel to jupyter
* ```jupyter sparqlkernel install --user zazuko```       add SPARQL kernel to jupyter
* ```jupyter notebook``` start a server

For more details on setting up a jupyer notebook in a virtual environment, look [here](https://janakiev.com/blog/jupyter-virtual-envs/).
For more details on installing the SPARQL kernel, look [here](http://www.bobdc.com/blog/jupytersparql/).

### Remotely
You can execute our notebooks in Google Colab environment. To run it in Colab, you will need to install all dependencies.
First, import `requirements.txt` to your workspace. Then install them. You can do it by running (in Colab):
```!pip install -r requirements.txt```

## Explore

We provide tutorials on datasets available as Linked Data.
These datasets are published together with various Swiss organizations.

Available tutorials are:

[Zürich Statistical Office](https://ld.stadt-zuerich.ch/org/SSZ):
* [Data model](notebooks/statistics-zurich/data_model.ipynb)
* [Population](notebooks/statistics-zurich/population.ipynb)
* [Real estate](notebooks/statistics-zurich/real_estate.ipynb)
* [Economy](notebooks/statistics-zurich/economy.ipynb)

[Federal Electricity Commission - ElCom](https://www.elcom.admin.ch/):

* [Electricity prices](notebooks/electricity-prices/electricity_prices.ipynb)

