
import streamlit as st


def run():

    st.write('Expander allows to hide optional controls')

    with st.echo():

        expander = st.expander("Optional controls")

        expander.radio("Day of week", ["Monday", "Tuesday", "Wednesday"])
