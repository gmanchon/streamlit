
import streamlit as st

def run():

    with st.echo():
        if st.button('click me'):
            # print is visible in server output, not in the page
            print('button clicked!')
            'I was clicked 🎉'
        else:
            'I was not clicked 😞'
