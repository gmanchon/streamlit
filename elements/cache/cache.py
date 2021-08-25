
import streamlit as st

import numpy as np
import pandas as pd


def title():
    return 'Cache 🚀'


def run():

    st.write('''
        Streamlit reruns the whole code of the page each time the user \
        interacts with a control. If the code of the page loads a dataset, \
        the dataset will be reloaded everytime the user uses a control. \
        How to deal with that?

        The `@st.cache` decorator allows the functions on which it is placed \
        to be executed only once and its result cached

        In the example below, both dataframes are created with random values. \
        Interacting with the slider shows that the top dataframe is \
        regenerated on every interaction, while the bottom dataframe is not
        ''')

    st.slider('Hi, I am a totally unrelated slider', 1, 10, 1)

    columns = st.columns(2)

    with st.echo():

        def get_data():
            return pd.DataFrame(
                    np.random.randn(3, 3),
                    columns=['a', 'b', 'c'])

        @st.cache
        def get_cached_data():
            return get_data()

        columns[0].write("Uncached dataframe")
        columns[0].write(get_data())

        columns[1].write("Cached dataframe")
        columns[1].write(get_cached_data())
