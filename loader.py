"""
loads all scripts in the components directory
retrieves their title and executes their run function
the directories and scripts are loaded in the order specified by order.json
"""

import streamlit as st

import os
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
        'scripts' : []
    }

    # loading order json file
    order = []
    order_path = join(path, 'order.json')

    if isfile(order_path):

        with open(order_path) as json_file:
            order = json.load(json_file)

    # listing entries in components directory
    entries = listdir(path)

    sorted_entries = []

    # ordering entries according to order json file
    for entry in order:

        # handling script files
        entry_path = join(path, entry)

        if not isdir(entry_path):
            entry += '.py'

        # adding sorted entry to result
        sorted_entries.append(entry)

        # removing sorted entry from order json list
        if entry in entries:
            entries.remove(entry)

    # adding unsorted entries back
    sorted_entries += entries

    # iterating through the content of the directory
    for entry in sorted_entries:

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
            containers['scripts'] += [{
                'type' : 'script',
                'name' : script_name,
                'path' : entry_path
            }]

    # buiding node list
    nodes = []

    nodes.append(containers['title'])
    nodes += containers['sections']
    nodes += containers['scripts']

    return nodes

def file_root_to_title(file_root):
    return file_root.replace('_', ' ').capitalize()

def file_name_to_title(file_path):
    file_root = split(file_path)[1][:-3] # remove path then remove .py
    return file_root_to_title(file_root)

def get_node_anchor(node):

    if 'title' in node:
        return node['title']

    return file_root_to_title(node['name'])

def load_script(script, run=True):
    """
    loads and executes script content
    script is expected to respond to the `title` and `run` functions
    """

    script_path = script['path']
    module_name = script_path.replace(os.sep, '.')

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
        script_title = file_name_to_title(script_path)

    # run script
    if run:

        # create script anchor for sidebar link
        st.write(f'<a name="{script_title}"></a>', unsafe_allow_html=True)

        # insert script title in page
        st.markdown(f'# {script_title}')

        # insert script content in page through its run function
        if hasattr(module, 'run'):
            module.run()

    # fill script info
    script['title'] = script_title

def populate_sidebar(nodes, magic_function):
    """
    adds links to the content of the scripts in the sidebar
    """

    # create menu
    menu_items = dict(
        Foreword=dict(
            function=magic_function))

    current_menu_item = ""

    # create sidebar table of content
    for node in nodes:

        node_type = node['type']

        if node_type == 'title':

            node_name = node['name'].capitalize()
            node_level = node['level']

            if node_level >= 3:
                node_level += 2

            toc_item = f"""<h{node_level}>{node_name}</h{node_level}>"""

            if node_level == 2:

                current_menu_item = node_name

                menu_items[current_menu_item] = dict(
                    name=current_menu_item,
                    nodes=[node],
                    toc_items=[toc_item])

            elif node_level > 2:

                # add sub headers to toc
                menu_items[current_menu_item]["toc_items"].append(toc_item)

        elif node_type == 'script':

            anchor = get_node_anchor(node)
            toc_item = f"""<a href="#{anchor}">{anchor}</a><br>"""

            menu_items[current_menu_item]["nodes"].append(node)
            menu_items[current_menu_item]["toc_items"].append(toc_item)

    # create menu
    menu_item = st.sidebar.radio("Menu", menu_items.keys())

    # show content
    selected_menu_item = menu_items[menu_item]

    menu_item_function = selected_menu_item.get("function")
    menu_item_name = selected_menu_item.get("name")
    menu_item_nodes = selected_menu_item.get("nodes")
    menu_item_toc_items = selected_menu_item.get("toc_items")

    if menu_item_function is not None:

        # hard coded toc allows to keep some widgets demo in the main file
        # useful in particular in order to demonstrate the magic commands
        hard_coded_toc = '''<h1>Foreword</h1>
            <a href="#Import">Import</a><br>
            <a href="#Magic commands">Magic commands</a><br>
            <a href="#Inline documentation">Inline documentation</a><br>
            <a href="#Echo">Echo</a><br>
        '''

        toc = hard_coded_toc

        # run magic function
        menu_item_function()

    else:

        st.write(f'# Streamlit quick reference - {menu_item_name}')

        # inject nodes
        for node in menu_item_nodes:

            # ignore non scripts
            if node['type'] != 'script':
                continue

            load_script(node, run=True)

        # inject menu items
        toc = "".join(menu_item_toc_items)

    st.sidebar.markdown(toc, unsafe_allow_html=True)

def load_components(magic_function):
    """
    executes all script files in the components directory
    """

    components_path = 'elements'
    components_level = 1

    # retrieve the list of script files
    nodes = recursive_iterate_directories(components_path, components_level)

    # load each script
    for node in nodes:

        # ignore non scripts
        if node['type'] != 'script':
            continue

        # load script title
        load_script(node, run=False)

    # the sidebar widgets in the components scripts gets injected in the sidebar
    # before the menu links because the scripts are loaded first
    # it is required to load the scripts first to retrieve their custom title

    # fill sidebar with links to script content
    populate_sidebar(nodes, magic_function)

    # st.write(nodes)
