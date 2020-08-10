
import streamlit as st

def run():

    with st.echo():
        import datetime

        t = st.time_input('Set an alarm for', datetime.time(8, 45))
        st.write('Alarm is set for', t)
