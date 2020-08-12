
import streamlit as st

def run():

    st.write('Allows to execute and render a block of code conditionally')

    with st.echo():
        if st.checkbox('Show content'):
            st.write('''
                This code will only be executed when the check box is checked

                Streamlit elements injected inside of this block of code will \
                not get displayed unless it is checked
                ''')
