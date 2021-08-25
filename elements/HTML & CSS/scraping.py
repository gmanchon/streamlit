
import streamlit as st

def title():
    return 'Scrapping Le Wagon Privacy Policy! 🥳'

def run():

    st.write('If you are seriously considering clicking these boxes (the second one first, for maximum efficiency), you are probably better off reading the [official documentation](https://docs.streamlit.io/en/stable/). It not, [here is the code](https://github.com/gmanchon/streamlit/blob/master/elements/advanced/scraping.py)')

    if st.checkbox('2. Inject the CSS for the privacy policy 😋'):
        st.write('<link href="https://www.iubenda.com/assets/privacy_policy-4925cabc28812855d7c0a24b1f0c961c.css" media="screen" rel="stylesheet" type="text/css" />', unsafe_allow_html=True)

    if st.checkbox('1. Inject the privacy policy 😋'):
        with st.echo():
            import requests
            from bs4 import BeautifulSoup

            @st.cache
            def get_scraping_data():

                url = 'https://www.iubenda.com/privacy-policy/7967062/legal'
                response = requests.get(url)

                soup = BeautifulSoup(response.content, 'html.parser')
                content = str(soup.select('#wbars_all'))

                return content

            content = get_scraping_data()

            st.write(f'<div id="iubenda_policy" class="iubenda_fixed_policy">{content}</div>', unsafe_allow_html=True)

