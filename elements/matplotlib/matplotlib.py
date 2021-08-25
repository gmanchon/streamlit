
import streamlit as st

def run():

    with st.echo():
        if st.checkbox('Show matplotlib', False):
            import matplotlib.pyplot as plt

            from scipy import misc

            fig, ax = plt.subplots()

            face = misc.face(gray=True)
            ax.imshow(face, cmap='gray')

            st.pyplot(fig)
        else:
            from PIL import Image
            image = Image.open('images/matplotlib.png')
            st.image(image, caption='matplotlib', use_column_width=False)
