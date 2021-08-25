
import streamlit as st

import numpy as np
import pandas as pd

def run():

    with st.echo():
        @st.cache
        def get_area_chart_data():
            print('get_area_chart_data called')
            return pd.DataFrame(
                    np.random.randn(20, 3),
                    columns=['a', 'b', 'c']
                )

        chart_data = get_area_chart_data()

        st.area_chart(chart_data)
