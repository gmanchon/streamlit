
import streamlit as st

import numpy as np
import pandas as pd


def run():

    with st.echo():

        @st.cache
        def get_histo():

            df = pd.DataFrame(
                    np.random.randn(200, 1),
                    columns=['a']
                )

            return np.histogram(
                df.a, bins=25)[0]

        hist_values = get_histo()

        st.bar_chart(hist_values)
