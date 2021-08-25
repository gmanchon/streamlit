
import streamlit as st

def run():

    with st.echo():

        import matplotlib.pyplot as plt

        from scipy import misc

        fig, ax = plt.subplots()

        face = misc.face(gray=True)
        ax.imshow(face, cmap='gray')

        st.pyplot(fig)
