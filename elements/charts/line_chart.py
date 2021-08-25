
import streamlit as st

import pandas as pd
import numpy as np


def run():

    with st.echo():

        @st.cache
        def get_line_chart_data():

            return pd.DataFrame(
                    np.random.randn(20, 3),
                    columns=['a', 'b', 'c']
                )

        df = get_line_chart_data()

        st.line_chart(df)
