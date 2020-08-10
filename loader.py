
import streamlit as st

from os import listdir
from os.path import isfile, isdir, join

def recursive_iterate_directories(path, level):
    """
    recursively iterates through directories
    returns a list of script files with attributes
    """

    scripts = []

    # iterating through the content of the directory
    for entry in listdir(path):

        entry_path = join(path, entry)

        # recursion on directories
        if isdir(entry_path):
            scripts += recursive_iterate_directories(entry_path, level + 1)

        # iterating through files in the component directory
        if isfile(entry_path):
            scripts += [{
                'path' : entry_path
            }]

    return scripts

def load_components():
    """
    executes all script files in the components directory
    """

    components_path = 'components'
    components_level = 0

    # retrieve the list of script files
    scripts = recursive_iterate_directories(components_path, components_level)

    st.write(scripts)
