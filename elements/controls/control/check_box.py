
import streamlit as st

def run():

    st.write('Allows to execute and render a block of code conditionally')

    with st.echo():
        if st.checkbox('Show content'):
            st.write('Any set of text or widgets')
