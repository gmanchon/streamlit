
import streamlit as st

def title():
    return 'Magnificent balloons 🎈'

def run():

    with st.echo():
        if st.button('More 🎈🎈🎈 please!'):
            st.balloons()
