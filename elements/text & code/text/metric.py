
import streamlit as st


def run():

    st.write('Allows to display metrics in bold font')

    with st.echo():

        col1, col2, col3 = st.columns(3)
        col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
        col2.metric("FTEC", "$121.10", "0.46%")
        col3.metric("BTC", "$46,583.91", "+4.87%")
