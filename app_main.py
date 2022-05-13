# Main app script

import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np

from app_location_selector import feature_location_selector

@st.cache(suppress_st_warning = True, allow_output_mutation = True)
def get_data():
    gdf = gpd.read_file("./geo_data/gadm36_PHL.gpkg")
    return gdf

if __name__ == "__main__":
    gdf = get_data()

    st.markdown("# GADM Location Selector")

    st.markdown("This web app allows you to select any administrative area in the Philippines and obtain its corresponding GID value from the GADM database. Buttons are provided so that you can copy the information with one click.")

    st.info("The source code for the app is publicly hosted on the following repository: https://github.com/MiguelAHG/gadm-location-selector\n\n We do not store data about the options that you choose on this app.")

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

    with st.expander("Credits", expanded = False):
        st.markdown("""This web app was developed by Miguel Antonio H. Germar as a supplement to another project. The location data used in this app is from the Global Administrative Areas (GADM) database, version 3.4, whose license permits non-commercial use only. The complete reference for GADM is shown below.\n\nUniversity of Berkeley, Museum of Vertebrate Zoology and the International Rice Research Institute. (2018, April). Global Administrative Areas (GADM) Version 3.4. GADM. https://gadm.org""")