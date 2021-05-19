# Linked Data by Zürich’s Statistic Office

[Zürich’s Statistic Office](https://www.stadt-zuerich.ch/prd/en/index/statistik.html) collects and publishes statistical information from all areas of life. That includes demographics, economy, construction, residency and politics. Corresponding datasets are publised as [Linked Data](https://en.wikipedia.org/wiki/Linked_data).

These tutorials show **how to work with Linked Data**. They demonstrate how to query data published by city of Zurich.
We recommend them to:

* Explore datasets from Zürich’s Statistic Office
* Retrieve data slices about demographics, real estate and economics
* Visualize these data slices

## SPARQL endpoint

If you are familiar with SPARQL, you can execute your queries here: https://ld.stadt-zuerich.ch/sparql/.
Our tutorials show how to work with SPAQRL directly in python.
## Install
### Locally
To setup the project locally:
* ```python3 -m venv venv``` create virtual environment
* ```source venv/bin/activate``` to activate venv on Linux or  ```venv\Scripts\activate.bat``` to activate venv on Windows
* ```pip install -r requirements.txt``` install dependencies
* ```python -m ipykernel install --user --name=ssz``` add your venv to jupyter
* ```jupyter notebook``` start a server

For more details on how to setup jupyer notebook in a virtual environment, look [here](https://janakiev.com/blog/jupyter-virtual-envs/)

### Remotely
You can execute all notebooks in Google Colab environment. To run it in Colab, you will need to install all dependencies.
First, import `requirements.txt` to your workspace. Then install them. You can do it by running (in colab):
```!pip install -r requirements.txt```

## Explore

We provide tutorials on data model, and data exploration.

Use data exploration tutorials to:
* learn how to work with SPARQL in python
* find demoraphics, economics, or real estate data
* learn about Zurich over time

Use data model tutorial if:
* you want to find other datasets about Zurich
* you don't know how to formulate queries to access it
### Data model

Here we explain the logic behind the Zürich's Linked Data model. This tutorial will guide you through the data structure. It will show you available datasets, and the shape they take. You will find there queries explaining data structure, and available dimensions.

The tutorials are:
* [Data model](notebooks/data_model.ipynb)

For this tutorial, choose kernel ```SPARQL```.
### Data exploration

These tutorials explore available datasets. You will see how to query, preprocess and visualize Zurich datasets. You will find there queries for specific observations.

Available tutorials are:
* [Population](notebooks/population.ipynb)
* [Real estate](notebooks/real_estate.ipynb)
* [Economy](notebooks/economy.ipynb)

For these tutorials, choose kernel ```ssz```.
