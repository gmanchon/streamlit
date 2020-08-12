
import streamlit as st

import pandas as pd
import numpy as np

@st.cache
def get_data():
    print('get_data line chart called')
    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

def run():

    with st.echo():
        df = get_data()

        st.line_chart(df)
