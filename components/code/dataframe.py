
import streamlit as st

import numpy as np
import pandas as pd

def run():

    with st.echo():
        df = pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

        st.table(df.head())

        df

    st.write('## Using Pandas Styler')

    with st.echo():
        dataframe = pd.DataFrame(
            np.random.randn(10, 20),
            columns=('col %d' % i for i in range(20)))

        st.dataframe(dataframe.style.highlight_max(axis=0))

