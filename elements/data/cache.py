
import streamlit as st

import numpy as np
import pandas as pd

def title():
    return 'Cache 🚀'

def run():

    st.write('''
        Streamlit is going to reinterpret the whole code generating the page \
        from scratch each time the user interacts with a control element \
        (slider, input, etc). This will cause the page to feel unresponsive \
        as its content grows

        For example, we do not want to load our whole dataset everytime
        the user switches the position of a slider. How to deal with that?

        The `@st.cache` decorator allows the functions on which it is placed \
        to be executed only once
        ''')

    st.write('''
        Let's take an example. The following dataframe gets constructed \
        on every user interaction of the user with any control element \
        in the page. The location of the element in the page does not matter

        Because the dataframe is not cached, its random data changes \
        on every user interaction, for example with this totally unrelated slider
        ''')

    with st.echo():
        df = pd.DataFrame(
                np.random.randn(3, 3),
                columns=['a', 'b', 'c'])

        st.write(df)

    st.slider('Hi, I am a totally unrelated slider', 1, 10, 1)

    st.write('''
        Try changing the radio buttons at the top of the sidebar... \
        They also change the content of dataframe because the code gets \
        reinterpreted each time the user interacts with a control element

        On the contrary, this second dataframe is returned by a function \
        decorated by `@st.cache`. Its content does not change \
        as the user slides. If the dataframe has a few million lines, \
        the difference will have a real impact on the responsiveness \
        of the page
        ''')

    with st.echo():
        @st.cache
        def get_cached_data():
            return pd.DataFrame(
                np.random.randn(3, 3),
                columns=['a', 'b', 'c'])

        cached_df = get_cached_data()

        st.write(cached_df)
