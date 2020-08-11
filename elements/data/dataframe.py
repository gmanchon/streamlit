
import streamlit as st

import numpy as np
import pandas as pd

def title():
    return 'DataFrame'

def run():

    st.write('## Default rendering')

    with st.echo():
        df = pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

        st.write(df)

    st.write('## Using a table')

    with st.echo():
        st.table(df.head())

    st.write('## Using pandas styler')

    with st.echo():
        df = pd.DataFrame(
            np.random.randn(10, 20),
            columns=('col %d' % i for i in range(20)))

        st.dataframe(df.style.highlight_max(axis=0))

