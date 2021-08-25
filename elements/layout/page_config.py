
import streamlit as st


def title():
    return 'Page configuration 🐍'


def run():

    st.write('🚧 Page configuration is a beta feature and should evolve soon 🚧')

    st.write('Page configuration allows to configure the favicon and title of the page in the browser tab, as well as the initial state of the sidebar and the general layout of the page')

    st.write('⚠️ `set_page_config` should be the first streamlit statement of the app ⚠️')

    st.code('''
        st.set_page_config(
            page_title="Quick reference", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed
        ''')
