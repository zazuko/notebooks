# Statistik Stadt Zurich datasets
Explore datasets from Statistik Stadt Zurich.
Retrieve data slices from population dataset with SPARQL.
Visualize age, gender, nationality, time and space dimensions.

# Install
To setup the project locally:
* ```python3 -m venv``` create virtual environment
* ```source venv/bin/activate``` to activate venv on Linux or  ```venv\Scripts\activate.bat``` to activate venv on Windows
* ```pip install -r requirements.txt``` install dependencies
* ```python -m ipykernel install --user --name=ssz``` add your venv to jupyter
* ```jupyter notebook``` start a server

For more details on how to setup jupyer notebook in a virtual environment, look [here](https://janakiev.com/blog/jupyter-virtual-envs/)

# Explore
To explore SPARQL queries, go to ```exploratory_queries.ipynb```. Required kernel: ```SPARQL```.
To explore data visualization, go to ```main.ipynb```. Required kernel: ```ssz```.


