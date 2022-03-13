# Main app script

import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np

from app_location_selector import location_selector_feature

if __name__ == "__main__":
    gdf = gpd.read_file("gadm36_PHL.gpkg")
    location_selector_feature(finest_level = 3, gdf = gdf)