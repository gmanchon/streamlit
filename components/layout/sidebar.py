
import streamlit as st

def run():

    with st.echo():
        st.sidebar.markdown(f"""
            # Header resizer
            Selected option: {{option}}
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
