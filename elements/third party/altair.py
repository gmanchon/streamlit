
import streamlit as st

import pandas as pd
import numpy as np

def title():
    return 'Altair, Vega Lite, Bokeh, pydeck, Deck GL, Graphviz'

def run():

    with st.echo():
        import altair as alt

        df = pd.DataFrame(
            np.random.randn(200, 3),
            columns=['a', 'b', 'c'])

        c = alt.Chart(df).mark_circle().encode(
            x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

        st.write(c)
