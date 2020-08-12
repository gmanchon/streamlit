
import streamlit as st

import numpy as np
import pandas as pd

def title():
    return 'DataFrame'

def run():

    st.write('## Default rendering')

    with st.echo():
        @st.cache
        def get_dataframe_data():
            print('get_dataframe_data called')
            return pd.DataFrame(
                    np.random.randn(10, 5),
                    columns=('col %d' % i for i in range(5))
                )

        df = get_dataframe_data()

        st.write(df.head())

    st.write('## Using a table')

    with st.echo():
        st.table(df.head())

    st.write('## Using pandas styler')

    with st.echo():
        st.dataframe(df.head().style.highlight_max(axis=0))
