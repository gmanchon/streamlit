
import streamlit as st

import pandas as pd
import numpy as np


def run():

    st.write('Here is a code sample for Altair, please refer to the [streamlit API reference](https://docs.streamlit.io/en/stable/api.html#display-charts) for other code samples')

    with st.echo():

        @st.cache
        def get_altair_data():

            return pd.DataFrame(
                    np.random.randn(200, 3),
                    columns=['a', 'b', 'c']
                )

        import altair as alt

        df = get_altair_data()

        c = alt.Chart(df).mark_circle().encode(
            x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

        st.write(c)
