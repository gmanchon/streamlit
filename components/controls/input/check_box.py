
import streamlit as st

def run():

    with st.echo():
        if st.checkbox('Show content'):
            st.write('Any set of text or widgets')
