"""
this is the main file, the only file in which the magic commands will work
the loader is used in order to load the scripts demonstrating each widget
"""

import streamlit as st

from loader import load_components

import time

# page conf
st.set_page_config(
    page_title="Quick reference",
    page_icon="🐍",
    layout="centered",  # wide
    initial_sidebar_state="auto")  # collapsed

# process page load duration
page_load_start_time = time.time()

st.sidebar.radio('Check load time', ('switch from one button to the other', 'in order to reinterpret the code'))

page_load_time_placeholder = st.sidebar.empty()


def magic_function():
    """
    the magic command syntax only works in the main file
    other files require the usage of st.write or st.markdown
    """

    st.markdown('# Streamlit quick reference')

    'This is just a quick demo. You should prefer the [official API reference](https://docs.streamlit.io/en/stable/api.html). Have a look at the [streamlit cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)'

    'The sidebar (arrow on the top left of the page) allows you to navigate in the page and displays the page load time. You may check how the prod location affects the load time: [EU version](https://wagon-data-streamlit-eu.herokuapp.com/) vs [US version](https://wagon-data-streamlit.herokuapp.com/)'

    'This app was [created using streamlit](https://www.imdb.com/title/tt1375666/). The code of the page is visible [here](https://github.com/gmanchon/streamlit). If you are just getting started, an older yet simpler version of the code is available [here](https://github.com/gmanchon/streamlit/tree/main)'

    st.write('<a name="Import"></a>', unsafe_allow_html=True)

    '# Import'

    st.code("import streamlit as st")

    st.write('<a name="Magic commands"></a>', unsafe_allow_html=True)

    '# Magic commands'

    'All strings or objects in the **main** script file will automatically be rendered in the page by streamlit as if `write` or `mardown` were used. This only works in the main file, other script files need to use `st.write` or `st.markdown` in order to display objects or text'

    with st.echo():
        'some text or **markdown**'

        {
            'hello': True
        }

    st.write('<a name="Inline documentation"></a>', unsafe_allow_html=True)

    '# Inline documentation'

    'Any streamlit method called without parenthesis and arguments will display its documentation'

    with st.echo():
        st.echo

    st.write('<a name="Echo"></a>', unsafe_allow_html=True)

    '# Echo'

    'Allows to display a block of code and then execute it. This is what is used on this page in order to demonstrate the usage of the various streamlit elements'

    with st.echo():
        with st.echo():
            st.write('hello 👋')


# load components from script files
load_components(magic_function)

# about
st.sidebar.write("# About")

st.sidebar.info("Streamlit quick reference")

# show page load duration in sidebar
page_load_duration = time.time() - page_load_start_time

page_load_time_placeholder.markdown(f'{round(page_load_duration, 3)} seconds')
