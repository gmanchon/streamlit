
import streamlit as st

def run():

    st.write('Since the streamlit elements are injected in the page in the order in which they are encountered in the code as it is being interpreted, they are displayed sequentially one after the other in the order in which they are in the code... Using placeholders allow to define a position in the page to display an element which will be filled later')

    st.write('This is what is used in order to display the page load time at the top of the sidebar, even though it is only processed once the page finished loading')

    st.markdown('`write`cannot be used on placeholders, use `markdown` instead')

    with st.echo():
        # this defines the location where the placeholded code will be displayed
        placeholder = st.empty()

        # this should be displayed before, according to its position in the code,
        # but gets displayed after because it is comes after the placeholder
        st.write('2. Some other element')

        placeholder.markdown('1. This gets displayed before even though it is called later')
