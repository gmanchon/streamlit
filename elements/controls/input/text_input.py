
import streamlit as st

def run():

    with st.echo():
        title = st.text_input('Movie title', 'Life of Brian')

        st.write('The current movie title is', title)
