
import streamlit as st


def title():
    return 'Password 🔑'


def run():

    st.write('## Protect your app with a password')

    st.write('A simple solution to protect your app without having to manage a database or user accounts is to use a password. In order to do so, you need to load the password from an environment variable and match it to the user input')

    st.write('Here is a [demo app](https://wagon-streamlit-auth.herokuapp.com/) and the [code of the repo](https://github.com/gmanchon/streamlit_auth)')
