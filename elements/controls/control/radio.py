
import streamlit as st

def run():

    st.write('Allows to execute and render a block of code depending on user choice')

    with st.echo():
        direction = st.radio('Select a direction', ('top', 'right', 'bottom', 'left'))

        st.write(direction)

        if direction == 'top':
            st.write('🔼')
        elif direction == 'right':
            st.write('▶️')
        elif direction == 'bottom':
            st.write('🔽')
        else:
            st.write('◀️')
