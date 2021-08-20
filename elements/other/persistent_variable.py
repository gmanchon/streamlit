import streamlit as st

def title():
    return 'Persistent variable using Sessiont State'

def run():
    st.write("Streamlit runs from top to bottom on every iteraction, and we lose track of variables, unless we use `session_state`")
    st.write("Here we create a persistent variable that you can increment/decrement, and which value will persist even after a rerun!")


    with st.echo():
                
        # We need to check if `persistent_variable` has already been initialized in `st.session_state`
        if 'persistent_variable' not in st.session_state:
            st.session_state.persistent_variable = 0

        increment = st.button('Increment')
        if increment:
            st.session_state.persistent_variable += 1

        decrement = st.button('Decrement')
        if decrement:
            st.session_state.persistent_variable -= 1

        st.write('Persistent variable = ', st.session_state.persistent_variable)
