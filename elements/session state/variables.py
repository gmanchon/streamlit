import streamlit as st

def title():
    return 'Session variables'

def run():

    st.write("The session state allows to persist variables between code reruns and for the duration of a user session. Without the session state, it would not be possible to easily store variables between two interactions with the components of the page")

    st.write("The session state starts empty for each user session")

    with st.echo():

        unpersisted_variable = 0  # here is how a normal variable behaves for comparison
        if "persisted_variable" not in st.session_state:
            st.session_state.persisted_variable = 0  # initialize the session state variable

        if st.button("Increment"):
            unpersisted_variable += 1
            st.session_state.persisted_variable += 1

        if st.button("Decrement"):
            unpersisted_variable -= 1
            st.session_state.persisted_variable -= 1

        st.write("Session state")

        st.write(st.session_state)

        st.write(f"Unpersistent variable: {unpersisted_variable} 👈 the value does not take into account previous page reruns")
        st.write(f"Persisted variable: {st.session_state.persisted_variable} 👈 the data is persisted between reruns")
        st.write(f'Persisted variable: {st.session_state["persisted_variable"]}')
