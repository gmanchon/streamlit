
import streamlit as st

def run():

    with st.echo():
        import datetime

        d = st.date_input(
            "When's your birthday",
            datetime.date(2019, 7, 6))
        st.write('Your birthday is:', d)
