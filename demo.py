"""
this is the main file, the only file in which the magic commands will work
the loader is used in order to load the scripts demonstrating each widget
"""

import streamlit as st

from loader import load_components

# this magic command syntax will only work in the main file, other files will require the usage of st.write or st.markdown
'# Streamlit quick reference'

'You should prefer the [official API reference](https://docs.streamlit.io/en/stable/api.html)'

st.write(f'<a name="Import"></a>', unsafe_allow_html=True)

'# Import'

with st.echo():
    import streamlit as st

st.write(f'<a name="Magic commands"></a>', unsafe_allow_html=True)

'# Magic commands'

'All strings in the **main** script file will be rendered in the page as markdown. Other script files need to use `st.markdown` or `st.write` in order to display text or other objects'

with st.echo():
    'some text or **markdown**'

st.write(f'<a name="Inline documentation"></a>', unsafe_allow_html=True)

'# Inline documentation'

'Any streamlit method called without parenthesis and arguments will display its documentation'

with st.echo():
    st.echo

st.write(f'<a name="Echo"></a>', unsafe_allow_html=True)

'# Echo'

'Allows to display a block of code and then execute it. This is what is used on this page in order to demonstrate the usage of the various streamlit elements'

with st.echo():
    with st.echo():
        st.write('hello 👋')

# load components from script files
load_components()
