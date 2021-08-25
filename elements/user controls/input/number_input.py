
import streamlit as st


def run():

    with st.echo():

        number = st.number_input('Insert a number')

        st.write('The current number is ', number)
