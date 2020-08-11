
import streamlit as st

def run():

    with st.echo():
        direction = st.radio('Select a direction', ('top', 'right', 'bottom', 'left'))
        st.write(direction)
