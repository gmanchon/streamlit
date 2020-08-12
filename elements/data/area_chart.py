
import streamlit as st

import numpy as np
import pandas as pd

@st.cache
def get_data():
    print('get_data area chart called')
    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

def run():

    with st.echo():
        chart_data = get_data()

        st.area_chart(chart_data)
