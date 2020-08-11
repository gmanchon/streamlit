"""
this is the main file, the only file in which the magic commands will work
the loader is used in order to load the scripts demonstrating each widget
"""

import streamlit as st

from loader import load_components

# this magic command syntax will only work in the main file, other files will require the usage of st.write or st.markdown
'# Streamlit quick reference'

'You should prefer the [official API reference](https://docs.streamlit.io/en/stable/api.html)'

'# Import'

with st.echo():
    import streamlit as st

'# Magic commands'

'All strings in the **main** script file will be rendered in the page as markdown. Other script files need to use `st.write` or `st.markdown` in order to display text or other objects'

with st.echo():
    'some text or **markdown**'

'# Echo'

'Display a block of executed code'

with st.echo():
    with st.echo():
        st.write('hello 👋')

# load components from script files
load_components()
