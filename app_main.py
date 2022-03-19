# Main app script

import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np

from app_location_selector import location_selector_feature

@st.cache(suppress_st_warning = True, allow_output_mutation = True)
def get_data():
    gdf = gpd.read_file("gadm36_PHL.gpkg")
    return gdf

if __name__ == "__main__":
    gdf = get_data()

    finest_level = st.radio(
        "Finest Level",
        options = [1, 2, 3],
    )

    location_selector_feature(finest_level = finest_level, gdf = gdf)