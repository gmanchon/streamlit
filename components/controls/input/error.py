
import streamlit as st

def title():
    return 'Error, warning, info, success'

def run():

    with st.echo():
        st.success('This is a success message!')
