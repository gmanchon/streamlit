
import streamlit as st

import numpy as np
import pandas as pd

import seaborn as sns


def title():
    return 'Pandas styler'


def run():

    with st.echo():

        @st.cache
        def get_dataframe_data():

            return pd.DataFrame(
                    np.random.randn(10, 5),
                    columns=('col %d' % i for i in range(5))
                )

        df = get_dataframe_data()

        cm = sns.color_palette("coolwarm_r", as_cmap=True)
        df = df.head().style.background_gradient(cmap=cm)

        st.write(df)
