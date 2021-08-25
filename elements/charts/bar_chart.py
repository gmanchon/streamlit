
import streamlit as st

import numpy as np
import pandas as pd


def run():

    with st.echo():

        @st.cache
        def get_bar_chart_data():

            return pd.DataFrame(
                    np.random.randn(50, 3),
                    columns=["a", "b", "c"]
                )

        chart_data = get_bar_chart_data()

        st.bar_chart(chart_data)
