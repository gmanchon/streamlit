
import streamlit as st

def title():
    return 'Functions ℱ'

def run():

    st.write('The `write` method allows to display any variable. Streamlit will have specific rendering adapted to the type of the variable, in particular for dataframes')

    with st.echo():
        def fun(a, b):
            '''docstring of the function'''
            return a + b

        st.write(fun)
