
import streamlit as st

def run():

    with st.echo():
        txt = st.text_area('Text to analyze', '''
            It was the best of times, it was the worst of times, it was
            the age of wisdom, it was the age of foolishness, (...)
            ''')
        st.write('Length:', len(txt))
