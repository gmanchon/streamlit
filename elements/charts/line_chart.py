
import streamlit as st

import pandas as pd
import numpy as np

def run():

    with st.echo():
        df = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c'])

        st.line_chart(df)
