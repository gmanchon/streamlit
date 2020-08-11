
import streamlit as st

def title():
    return 'Styling your pages with CSS 🤩'

def run():

    with st.echo():
        CSS = """
        h1 {
            color: red;
        }
        body {
            background-image: url(https://avatars1.githubusercontent.com/u/9978111?v=4);
            background-size: cover;
        }
        """

        if st.checkbox('Inject CSS'):
            st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
