
import streamlit as st

def run():

    with st.echo():
        dictionary = { 'a' : 1, 'b' : 2 }

        st.write(dictionary)
