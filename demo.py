
import streamlit as st

import numpy as np
import pandas as pd

'# Inline documentation'

'Any streamlit method called without parenthesis and arguments will display its documentation'

with st.echo():
    st.echo

'# Markdown'

'Markdown allows to structure your app into sections'

with st.echo():
    """
    # title

    ## many levels of subtitles

    **bold** or *italic* text with [links](http://github.com/streamlit) and:
    - bullet points
    """

'# Code'

'Display blocks of executed code'

with st.echo():
    with st.echo():
        st.write('hey')

'# DataFrame'

with st.echo():
    df = pd.DataFrame({
      'first column': list(range(1, 11)),
      'second column': np.arange(10, 101, 10)
    })

    df

'# Check box'

with st.echo():
    if st.checkbox('Show content'):
        'Any set of text or widgets'

'# Select box'

with st.echo():
    option = st.selectbox('Select a line to filter', df['first column'])

    df[df['first column'] == option]

'# Slider'

with st.echo():
    option = st.slider('Select a modulus', 1, 10, 3)

    df[df['first column'] % option == 0]

'# Line chart'

with st.echo():
    df = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

    st.line_chart(df)

'# Map'

with st.echo():
    map_df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_df)

'# Cache'

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

'# Sidebar'

with st.echo():
    st.sidebar.markdown(f"""
        # Title
        Selected option: {option}
        """)

'# Styling your pages with CSS 🤩'

with st.echo():
    CSS = """
    h1 {
        color: red;
    }
    body {
        background-image: url(https://avatars1.githubusercontent.com/u/9978111?v=4);
        background-size: cover;
    }
    """

    if st.checkbox('Inject CSS'):
        st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'# Scrapping Le Wagon Privacy Policy! 🥳'

if st.checkbox('Inject the CSS for the privacy policy 😋'):
    st.write('<link href="https://www.iubenda.com/assets/privacy_policy-4925cabc28812855d7c0a24b1f0c961c.css" media="screen" rel="stylesheet" type="text/css" />', unsafe_allow_html=True)

if st.checkbox('Inject the privacy policy 😋'):
    with st.echo():
        import requests
        from bs4 import BeautifulSoup

        response = requests.get('https://www.iubenda.com/privacy-policy/7967062/legal')

        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.select('#wbars_all')

        st.write(f'<div id="iubenda_policy" class="iubenda_fixed_policy">{str(content)}</div>', unsafe_allow_html=True)
