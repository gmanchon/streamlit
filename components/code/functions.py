
import streamlit as st

def title():
    return 'Functions ℱ'

def run():
    with st.echo():
        def fun(a, b):
            '''docstring of the function'''
            return a + b

        st.write(fun)
