
import streamlit as st

import numpy as np
import pandas as pd

def run():

    with st.echo():
        map_df = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon'])

        st.map(map_df)
