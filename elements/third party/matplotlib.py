
import streamlit as st

def run():

    with st.echo():
        import matplotlib.pyplot as plt

        from scipy import misc

        face = misc.face(gray=True)
        plt.imshow(face, cmap='gray')

        st.pyplot()
