
import streamlit as st

def title():
    return 'Error, warning, info, success'

def run():

    with st.echo():
        st.success('This is a success!')
        st.info('This is an info')
        st.warning('This is a semi success')
        st.error('Let\'s keep positive, this might be pretty close to a success!')
