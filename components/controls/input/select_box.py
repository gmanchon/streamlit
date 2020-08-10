
import streamlit as st

import numpy as np
import pandas as pd

def title():
    return 'Select box, multi select'

def run():

    with st.echo():
        df = pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

        option = st.selectbox('Select a line to filter', df['first column'])

        df[df['first column'] == option]
