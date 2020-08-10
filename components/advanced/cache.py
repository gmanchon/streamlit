
import streamlit as st

import numpy as np
import pandas as pd

def title():
    return 'Cache 🚀'

def run():

    with st.echo():
        df = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c'])

        df

    st.slider('Show me uncached changes', 1, 10, 1)

    with st.echo():
        @st.cache
        def get_data():
            return pd.DataFrame(
                np.random.randn(20, 3),
                columns=['a', 'b', 'c'])

        cached_df = get_data()

        cached_df

    option = st.slider('Zoom', 1, 10, 1)

    '### Uncached random df'

    st.line_chart(df)

    '### Cached random df'

    st.line_chart(cached_df)

    '### Impact of slider on cached df'

    new = cached_df.copy(True)
    new['a'] = cached_df['a'] / option

    st.line_chart(new)
