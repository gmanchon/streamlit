
import streamlit as st

def run():

    with st.echo():
        if st.checkbox('Show matplotlib', False):
            import matplotlib.pyplot as plt

            from scipy import misc

            face = misc.face(gray=True)
            plt.imshow(face, cmap='gray')

            st.pyplot()
        else:
            from PIL import Image
            image = Image.open('images/matplotlib.png')
            st.image(image, caption='matplotlib', use_column_width=False)
