
import streamlit as st

def render_sidebar():
    """
    manually creates sidebar content
    """

    TOC_HTML = """
    # Widgets
    <h3>Text</h3>
    <ul>
        <li><a href="#Inline documentation">Inline documentation</a></li>
        <li><a href="#Magic commands">Magic commands</a></li>
        <li><a href="#Text">Text</a></li>
        <li><a href="#Markdown">Markdown</a></li>
        <li><a href="#Latex">Latex</a></li>
    </ul>
    <h3>Code</h3>
    <ul>
        <li><a href="#Functions">Functions</a></li>
        <li><a href="#Objects">Objects</a></li>
        <li><a href="#Json">Json</a></li>
        <li><a href="#Echo">Echo</a></li>
        <li><a href="#Code">Code</a></li>
        <li><a href="#DataFrame">DataFrame</a></li>
    </ul>
    <h3>Controls</h3>
    <ul>
        <li><a href="#Check box">Check box</a></li>
        <li><a href="#Radio">Radio</a></li>
        <!--<li><a href="#Spinner">Spinner</a></li>-->
        <li><a href="#Progress bar">Progress bar</a></li>
        <li><a href="#Button">Button</a></li>
        <li><a href="#Select box, multi select">Select box, multi select</a></li>
        <li><a href="#Slider">Slider</a></li>
        <li><a href="#Text input">Text input</a></li>
        <li><a href="#Text area">Text area</a></li>
        <li><a href="#Number input">Number input</a></li>
        <li><a href="#Date input">Date input</a></li>
        <li><a href="#Time input">Time input</a></li>
        <li><a href="#File uploader">File uploader</a></li>
        <li><a href="#Error, warning, info, success">Error, warning, info, success</a></li>
    </ul>
    <h3>Charts</h3>
    <ul>
        <li><a href="#Line chart">Line chart</a></li>
        <li><a href="#Area chart">Area chart</a></li>
        <li><a href="#Bar chart">Bar chart</a></li>
        <li><a href="#Map">Map</a></li>
    </ul>
    <h3>Cache 🚀</h3>
    <ul>
        <li><a href="#Cache">Cache</a></li>
    </ul>
    <h3>Sidebar</h3>
    <ul>
        <li><a href="#Sidebar">Sidebar</a></li>
    </ul>
    <h3>Advanced</h3>
    <ul>
        <li><a href="#Styling your pages with CSS 🤩">Styling your pages with CSS 🤩</a></li>
        <!--<li><a href="#Using sections">Using sections</a></li>-->
        <li><a href="#Injecting HTML 🧙‍♂️">Injecting HTML 🧙‍♂️</a></li>
        <li><a href="#Scrapping Le Wagon Privacy Policy! 🥳">Scrapping Le Wagon Privacy Policy! 🥳</a></li>
    </ul>
    <h3>Third Party</h3>
    <ul>
        <li><a href="#Matplotlib">Matplotlib</a></li>
        <li><a href="#Plotly">Plotly</a></li>
        <li><a href="#Altair, Vega Lite, Bokeh, pydeck, Deck GL, Graphviz">Altair, Vega Lite, Bokeh, pydeck, Deck GL, Graphviz</a></li>
    </ul>
    <h3>Other</h3>
    <ul>
        <li><a href="#Images, Audio, Video">Images, Audio, Video</a></li>
        <li><a href="#Screencast">Screencast</a></li>
        <li><a href="#Magnificent balloons">Magnificent balloons</a></li>
        <li><a href="#Inspiration">Inspiration</a></li>
    </ul>
    """

    st.sidebar.markdown(TOC_HTML, unsafe_allow_html=True)
