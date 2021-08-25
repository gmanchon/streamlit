
import streamlit as st


def title():
    return 'Magnificent balloons 🎈'


def run():

    st.write('You\'re welcome 🙌')

    with st.echo():

        if st.button('More 🎈🎈🎈 please!'):
            st.balloons()
