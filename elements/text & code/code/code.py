
import streamlit as st


def run():

    with st.echo():

        st.code('''
            def function sum(a, b):
                return a + b
        ''')
