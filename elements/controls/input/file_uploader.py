
import streamlit as st

def run():

    with st.echo():
        st.set_option('deprecation.showfileUploaderEncoding', False)
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.write(data)
