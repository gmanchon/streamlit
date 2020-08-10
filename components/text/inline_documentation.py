
import streamlit as st

def run():
    st.write('Any streamlit method called without parenthesis and arguments will display its documentation')

    with st.echo():
        st.echo
