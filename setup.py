from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    # streamlit
    'streamlit==0.65.2',
    # data manipulation
    'numpy==1.18.4',
    'pandas==0.24.2',
    # data viz
    'matplotlib==3.2.1',
    'plotly==4.6.0',
    'altair==4.1.0',
    # computation
    'scipy==1.2.2',
    # scraping
    'requests==2.23.0',
    'bs4==0.0.1']

setup(
    name='WagonDataStreamlitDemo',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Wagon Data Streamlit Demo'
)
