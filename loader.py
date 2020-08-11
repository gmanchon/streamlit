"""
loads all scripts in the components directory
retrieves their title and executes their run function
"""

import streamlit as st

from os import listdir
from os.path import isfile, isdir, join, split

import importlib.util

import json

def recursive_iterate_directories(path, level):
    """
    recursively iterates through directories
    returns a list of script files with attributes
    """

    containers = {
        'title' : {
            'type' : 'title',
            'name' : split(path)[1],
            'level' : level,
        },
        'sections' : [],
        'scripts' : {}
    }

    # loading order json file
    order = []
    order_path = join(path, 'order.json')

    if isfile(order_path):

        with open(order_path) as json_file:
            order = json.load(json_file)

    # iterating through the content of the directory
    for entry in listdir(path):

        # ignore pycache directories
        if entry == '__pycache__':
            continue

        # ignore order file
        if entry == 'order.json':
            continue

        entry_path = join(path, entry)

        # recursion on directories
        if isdir(entry_path):
            containers['sections'] += recursive_iterate_directories(entry_path, level + 1)

        # ignoring non script files
        if entry_path[-3:] != '.py':
            continue

        # adding script files to the result
        if isfile(entry_path):
            script_name = entry[:-3]
            containers['scripts'][script_name] = {
                'type' : 'script',
                'name' : script_name,
                'path' : entry_path
            }

    # changing scripts order according to order json file
    container_scripts = containers['scripts']

    ordered_containers = []

    # ordering scripts specified in the order json file
    for script in order:

        # ignoring typos
        if script not in container_scripts:
            continue

        script_element = container_scripts[script]
        del(container_scripts[script])
        ordered_containers.append(script_element)

    # adding unspecified scripts at the end in the same order
    for key, value in container_scripts.items():

        ordered_containers.append(value)

    # buiding node list
    nodes = []

    nodes.append(containers['title'])
    nodes += containers['sections']
    nodes += ordered_containers

    return nodes

def file_root_to_title(file_root):
    return file_root.replace('_', ' ').capitalize()

def file_name_to_title(file_path):
    file_root = split(file_path)[1][:-3] # remove path then remove .py
    return file_root_to_title(file_root)

def get_node_anchor(node):

    if 'title' in node:
        return node['title'].capitalize()

    return file_root_to_title(node['name'])

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
        script_title = module.title().capitalize()
    else:
        # convert file name to title name
        script_title = file_name_to_title(script_path)

    # create script anchor for sidebar link
    st.write(f'<a name="{script_title}"></a>', unsafe_allow_html=True)

    # insert script title in page
    st.markdown(f'# {script_title}')

    # insert script content in page through its run function
    if hasattr(module, 'run'):
        module.run()

    # fill script info
    script['title'] = script_title

def populate_sidebar(nodes):
    """
    adds links to the content of the scripts in the sidebar
    """

    toc = ''

    # create sidebar table of content
    for node in nodes:

        node_type = node['type']

        if node_type == 'title':

            node_name = node['name'].capitalize()
            node_level = node['level']

            if node_level >= 3:
                node_level += 2

            toc += f"""<h{node_level}>{node_name}</h{node_level}>"""

        elif node_type == 'script':
            anchor = get_node_anchor(node)
            toc += f"""<a href="#{anchor}">{anchor}</a><br>"""

    st.sidebar.markdown(toc, unsafe_allow_html=True)

def load_components():
    """
    executes all script files in the components directory
    """

    components_path = 'components'
    components_level = 1

    # retrieve the list of script files
    nodes = recursive_iterate_directories(components_path, components_level)

    # load each script
    for node in nodes:

        # ignore non scripts
        if node['type'] != 'script':
            continue

        load_script(node)

    # fill sidebar with links to script content
    populate_sidebar(nodes)

    # st.write(nodes)
