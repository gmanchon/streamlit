
import streamlit as st

import numpy as np
import pandas as pd

@st.cache
def get_data():
    print('get_data slider called')
    return pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

def run():

    with st.echo():
        df = get_data()

        option = st.slider('Select a modulus', 1, 10, 3)

        filtered_df = df[df['first column'] % option == 0]

        st.write(filtered_df)
