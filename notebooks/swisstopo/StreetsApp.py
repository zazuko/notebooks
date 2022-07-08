import folium
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

from client import LindasClient
from utils import plot_streets_heatmap

client = LindasClient("https://ld.admin.ch/query")


@st.cache
def load_data():
    data = client.get_communes()
    return dict(zip(data.municipality, data.municipality_id))


def update_commune():

    # st.info(f"Loading commune: {muni2id[st.session_state.commune]}")
    centroid = client.get_commune_centroid(f"<{muni2id[st.session_state.commune]}>")
    df = client.get_commune_streets(f"<{muni2id[st.session_state.commune]}>")
    st.session_state.map = plot_streets_heatmap(centroid, df)


if "map" not in st.session_state:
    st.session_state.map = folium.Map(
        location=[46.837545, 8.197028], zoom_start=8.5, tiles="CartoDBdark_matter"
    )

st.set_page_config(layout="wide")

muni2id = load_data()
add_selectbox = st.sidebar.selectbox(
    "What commune would you like to be visualize?",
    key="commune",
    options=(*muni2id.keys(),),
    on_change=update_commune,
)
st_data = st_folium(st.session_state.map)


make_map_responsive = """
 <style>
 [title~="streamlit_folium.st_folium"] { width: 100%}
 </style>
"""
st.markdown(make_map_responsive, unsafe_allow_html=True)


# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text("Loading data...")
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Loading data...done!")
