
import streamlit as st

import pandas as pd
import numpy as np

def title():
    return 'Altair, Vega Lite, Bokeh, pydeck, Deck GL, Graphviz'

def run():

    st.write('Here is a code sample for Altair, please refer to the [streamlit API reference](https://docs.streamlit.io/en/stable/api.html#display-charts) for other code samples')

    with st.echo():
        @st.cache
        def get_altair_data():
            print('get_altair_data called')
            return pd.DataFrame(
                    np.random.randn(200, 3),
                    columns=['a', 'b', 'c']
                )

        if st.checkbox('Show altair', False):
            import altair as alt

            df = get_altair_data()

            c = alt.Chart(df).mark_circle().encode(
                x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

            st.write(c)
        else:
            from PIL import Image
            image = Image.open('images/altair.png')
            st.image(image, caption='altair', use_column_width=False)
