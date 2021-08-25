
import streamlit as st


def run():

    st.write('Using columns allows to display widgets side by side')

    with st.echo():

        columns = st.columns(3)

        first_name = columns[0].text_input("First name", value="John")
        columns[0].write(first_name)

        last_name = columns[1].text_input("Last name", value="Doe")
        columns[1].write(last_name)

        location = columns[2].text_input("Location", value="Paris")
        columns[2].write(location)
