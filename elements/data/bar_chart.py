
import streamlit as st

import numpy as np
import pandas as pd

@st.cache
def get_histo():
    print('get_histo bar chart called')
    df = pd.DataFrame(
            np.random.randn(200, 1),
            columns=['a']
        )

    return np.histogram(
        df.a, bins=25)[0]

@st.cache
def get_data():
    print('get_data bar chart called')
    return pd.DataFrame(
            np.random.randn(50, 3),
            columns=["a", "b", "c"]
        )

def run():

    with st.echo():
        hist_values = get_histo()

        st.bar_chart(hist_values)

    with st.echo():
        chart_data = get_data()

        st.bar_chart(chart_data)
