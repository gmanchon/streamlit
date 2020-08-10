
import streamlit as st

def run():

    st.write('Markdown allows to structure your app into sections')

    with st.echo():
        st.markdown("""
        # title

        ## many levels of subtitles

        **bold** or *italic* text with [links](http://github.com/streamlit) and:
        - bullet points
        """)
