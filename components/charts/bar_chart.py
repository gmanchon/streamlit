
import streamlit as st

import numpy as np
import pandas as pd

def run():

    with st.echo():
        df = pd.DataFrame(
                np.random.randn(200, 1),
                columns=['a'])

        hist_values = np.histogram(
            df.a, bins=25)[0]

        st.bar_chart(hist_values)

    with st.echo():
        chart_data = pd.DataFrame(
            np.random.randn(50, 3),
            columns=["a", "b", "c"])

        st.bar_chart(chart_data)
