# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Matematyka'
copyright = '2023-2025, Maciej Szeptuch'
author = 'Maciej Szeptuch'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "sphinx.ext.githubpages",
        #"sphinxcontrib.images", # https://github.com/sphinx-contrib/images
        "myst_parser",
        #"cloud_sptheme.ext.issue_tracker",
        "myst_parser" # ref: https://www.sphinx-doc.org/en/master/usage/markdown.html
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'pl'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['docs', 'Thumbs.db', '.DS_Store', '_build', 'venv', "README.md", "assets/README.md"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# more themes: https://sphinx-themes.org/#theme-groundwork-sphinx-theme
html_theme = 'cloud'
html_theme_options = {
        "sidebar_localtoc_title": "Spis treści:",
        "sidebar_prev_title": "Poprzednia strona",
        "sidebar_next_title": "Następna strona",
}
html_css_files= [
        'css/custom.css'
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "./assets/logo.png"
html_favicon = "./assets/icon.ico"
#TODO: add something better
#html_permalinks_icon=
html_copy_source=False

# for cloud_sptheme.ext.issue_tracker
issue_tracker_url="gh:gucio321/fizyka"

# for myst_parser (markdown)
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    #"linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

latex_elements = {
        'preamble': r'''
        \usepackage{cancel}
        \usepackage{braket}
        ''',
}
