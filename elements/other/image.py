
import streamlit as st

def title():
    return 'Images, Audio, Video'

def run():

    with st.echo():
        from PIL import Image
        image = Image.open('wagon.png')
        st.image(image, caption='Le Wagon', use_column_width=False)
