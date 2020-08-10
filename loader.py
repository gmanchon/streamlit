"""
loads all scripts in the components directory
retrieves their title and executes their run function
"""

import streamlit as st

from os import listdir
from os.path import isfile, isdir, join, split

import importlib.util

def recursive_iterate_directories(path, level):
    """
    recursively iterates through directories
    returns a list of script files with attributes
    """

    scripts = []

    # iterating through the content of the directory
    for entry in listdir(path):

        # ignore pycache directories
        if entry == '__pycache__':
            continue

        entry_path = join(path, entry)

        # recursion on directories
        if isdir(entry_path):
            scripts += recursive_iterate_directories(entry_path, level + 1)

        # ignoring non script files
        if entry_path[-3:] != '.py':
            continue

        # adding script files to the result
        if isfile(entry_path):
            scripts += [{
                'path' : entry_path
            }]

    return scripts

def load_script(script):
    """
    loads and executes script content
    script is expected to respond to the `title` and `run` functions
    """

    script_path = script['path']
    module_name = script_path.replace('/', '.')

    # load script
    # from https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # retrieve script title
    if hasattr(module, 'title'):
        script_title = module.title()
    else:
        # convert file name to title name
        script_title = split(script_path)[1].strip('.py').replace('_', ' ').capitalize()

    # create script anchor for sidebar link
    st.write(f'<a name="{script_title}"></a>', unsafe_allow_html=True)

    # insert script title in page
    st.markdown(f'# {script_title}')

    # insert script content in page through its run function
    if hasattr(module, 'run'):
        module.run()

    # fill script info
    script['title'] = script_title

def populate_sidebar(scripts):
    """
    adds links to the content of the scripts in the sidebar
    """
    pass

def load_components():
    """
    executes all script files in the components directory
    """

    components_path = 'components'
    components_level = 0

    # retrieve the list of script files
    scripts = recursive_iterate_directories(components_path, components_level)

    # load each script
    for script in scripts:
        load_script(script)

    # fill sidebar with links to script content
    populate_sidebar(scripts)

    st.write(scripts)
