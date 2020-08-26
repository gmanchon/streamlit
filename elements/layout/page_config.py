
import streamlit as st

def title():
    return 'Page configuration 🐍'

def run():

    st.write('🚧 Page configuration is a beta feature and should evolve soon 🚧')

    st.write('Page configuration allows to configure the favicon and title of the page in the browser tab')

    st.write('⚠️ `beta_set_page_config` should be the first streamlit statement of the app ⚠️')

    st.code('''
        st.beta_set_page_config(
            page_title="Quick reference", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed
        ''')
