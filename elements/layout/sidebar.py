
import streamlit as st

def run():

    st.write('Any of the streamlit elements can be inserted in the sidebar using `st.sidebar` as a prefix (except `write`, `echo` and `spinner`)')

    st.write('This content is visible at the top of the sidebar (arrow on the top left of the page). The slider displayed controls the size of the headers of the page through the CSS injected just below')

    with st.echo():
        st.sidebar.markdown(f"""
            # Header resizer
            """)

        font_size = st.sidebar.slider('Changer header size', 16, 72, 36)

        FONT_SIZE_CSS = f"""
        <style>
        h1 {{
            font-size: {font_size}px !important;
        }}
        </style>
        """
        st.write(FONT_SIZE_CSS, unsafe_allow_html=True)
