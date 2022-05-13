# Main app script

import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np

from app_location_selector import feature_location_selector

@st.cache(suppress_st_warning = True, allow_output_mutation = True)
def get_data():
    gdf = gpd.read_file("gadm36_PHL.gpkg")
    return gdf

if __name__ == "__main__":
    gdf = get_data()

    st.markdown("# GADM Location Selector")

    level_names = pd.Series(
        {
            1: "province",
            2: "city or municipality",
            3: "barangay",
        }
    )

    finest_level = st.radio(
        "Select level of location",
        options = level_names.index,
        format_func = lambda x: level_names[x],
    )

    feature_location_selector(
        gdf = gdf,
        finest_level = finest_level,
        level_names = level_names,
    )