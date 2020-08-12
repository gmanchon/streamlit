"""
this is the main file, the only file in which the magic commands will work
the loader is used in order to load the scripts demonstrating each widget
"""
#
import streamlit as st

from loader import load_components

import time

# process page load duration

page_load_start_time = time.time()

st.sidebar.radio('Check load time', ('switch from one button to the other', 'in order to reinterpret the code'))

page_load_time_placeholder = st.sidebar.empty()

# this magic command syntax will only work in the main file, other files will require the usage of st.write or st.markdown
'# Streamlit quick reference'

'This is just a quick demo. You should prefer the [official API reference](https://docs.streamlit.io/en/stable/api.html)'

'The sidebar (arrow on the top left of the page) allows you to navigate in the page'

'This app was [created using streamlit](https://www.imdb.com/title/tt1375666/). The code of the page is visible [here](https://github.com/gmanchon/streamlit). If you are just getting started, an older yet simpler version of the code is available [here](https://github.com/gmanchon/streamlit/tree/main)'

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

# show page load duration in sidebar
page_load_duration = time.time() - page_load_start_time

page_load_time_placeholder.markdown(f'{round(page_load_duration, 2)} seconds')
#
