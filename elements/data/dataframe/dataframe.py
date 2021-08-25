
import streamlit as st

import numpy as np
import pandas as pd


def title():
    return 'DataFrame'


def run():

    with st.echo():

        @st.cache
        def get_dataframe_data():

            return pd.DataFrame(
                    np.random.randn(10, 5),
                    columns=('col %d' % i for i in range(5))
                )

        df = get_dataframe_data()

        st.write(df.head())
