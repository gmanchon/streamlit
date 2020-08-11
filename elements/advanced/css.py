
import streamlit as st

def title():
    return 'Styling your pages with CSS 🤩'

def run():

    st.write('As an intermediary step between streamlit and pulling a micro or full web framework with Flask or Django, you can customize your app to a large extent using CSS')

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
