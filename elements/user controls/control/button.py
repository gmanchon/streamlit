
import streamlit as st


def run():

    with st.echo():

        if st.button('click me'):
            # print is visible in the server output, not in the page
            print('button clicked!')
            st.write('I was clicked 🎉')
            st.write('Further clicks are not visible but are executed')
        else:
            st.write('I was not clicked 😞')
