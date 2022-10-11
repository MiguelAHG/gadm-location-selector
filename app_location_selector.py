# Location selector feature

import streamlit as st
import pandas as pd
import numpy as np

def feature_location_selector(gdf, finest_level, level_names):
    """Location selector feature of the app.

Parameters
gdf: geopandas DataFrame, table of GADM data.
finest_level: integer, representation of the level of the location, from 1 to 3.
level_names: pandas Series, with level numbers in the index and level names in the values."""

    # List of columns to take from GDF.
    # Should include only GID and NAME columns down to the finest level.
    gdf_cols = [
        s.format(level)
        for level in range(1, finest_level + 1)
        for s in ["GID_{}", "NAME_{}"]
    ]

    gdf_subset = gdf[gdf_cols].copy()

    filtered_level_names = level_names[:finest_level]

    gid_list = []

    # Note that "name" here refers to location name.
    name_list = []

    for level in range(1, finest_level + 1):
        st_cols = st.columns(2)

        name_label = f"NAME_{level}"
        gid_label = f"GID_{level}"
        cat = filtered_level_names[level]

        with st_cols[0]:
            cur_name = st.selectbox(
                cat.title(),
                options = gdf_subset[name_label].unique(),
                # Use a key so that multiple instances of selectboxes are not connected.
                key = "/".join(gid_list),
            )

        gdf_subset = gdf_subset.loc[gdf_subset[name_label] == cur_name]

        gid_value = (gdf_subset.loc[:, gid_label].iloc[0])

        gid_list.append(gid_value)
        name_list.append(cur_name)

        full_location_name = ", ".join(reversed(name_list))

        # Display the full location name and GID.
        # Provide a button to copy each of these to the clipboard.

        name_descriptor = f"{cat.title()} Name"
        gid_descriptor = f"GID_{level} value"

        display_dict = {
            name_descriptor: full_location_name,
            gid_descriptor: gid_value,
        }

        with st_cols[1]:

            for info_type, info_value in display_dict.items():

                st.markdown(f"{info_type}: `{info_value}`")

                # # Button to copy text to clipboard. Commented out because it doesn't work in the Streamlit app deployed online.
                # clipboard_button = st.button(
                #     f"Copy {info_type} to Clipboard",
                #     key = f"clipboard_button {level} {info_type}",
                # )

                # if clipboard_button:
                #     cb_df = pd.DataFrame([info_value])
                #     cb_df.to_clipboard(index = False, header = False)

        # Use a line to separate the levels from each other.
        st.markdown("---")