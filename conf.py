# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pytest tutorial'
copyright = '2026, Kristian Rother'
author = 'Kristian Rother'
release = '1.0'
html_title = project

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'myst_parser',
    'sphinxcontrib.cairosvgconverter',
    ]


templates_path = ['_templates']
exclude_patterns = ['README.md', '_build', 'Thumbs.db', '.DS_Store', 'de/*', 'exercises/*', '.venv/*']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "_static/academis_logo.png"
html_favicon = "_static/favicon.ico"

html_css_files = [
    "academis.css",
]

html_theme_options = {
    "source_branch": "master",
    'logo': 'academis.png',
    'github_user': 'krother',
    'show_relbar_top' : True,
    'show_relbar_bottom' : True,
    "source_repository": "https://github.com/krother/python_testing_tutorial",
    "source_directory": "",
}
