
import streamlit as st

def title():
    return 'Images, Audio, Video'

def run():

    st.write('Please refer to the [streamlit API reference](https://docs.streamlit.io/en/stable/api.html#display-media) for more audio or video code samples')

    with st.echo():
        from PIL import Image
        image = Image.open('images/wagon.png')
        st.image(image, caption='Le Wagon', use_column_width=False)
