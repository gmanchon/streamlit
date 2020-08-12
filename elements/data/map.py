
import streamlit as st

import numpy as np
import pandas as pd

@st.cache
def get_data():
    print('get_data map called')
    return pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )

def run():

    with st.echo():
        if st.checkbox('Show map', True):
            df = get_data()

            st.map(df)
