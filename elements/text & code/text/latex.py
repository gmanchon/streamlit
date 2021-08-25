
import streamlit as st


def title():
    return 'LaTeX \\'


def run():

    st.write('Latex allows to display styled and structured text in your app, and is very useful in particular in order to display mathematical formulas')

    with st.echo():

        st.latex(r'''
            a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
            \sum_{k=0}^{n-1} ar^k =
            a \left(\frac{1-r^{n}}{1-r}\right)
            ''')
