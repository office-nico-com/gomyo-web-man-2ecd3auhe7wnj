import sys
import os
sys.path.append(os.path.abspath('.'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '五明原価管理ツール'
project_sub = '操作マニュアル'
copyright = '2026 System Design Office NICO. All rights reserved.'
# author = 'Fujisawa'
release = '1.0.0'
numfig = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['replace_in_headers']

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_context = {
    'project_sub': project_sub,
}
html_title = f"{project}"
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_css_files = ['custom.css']
html_extra_path = ["robots.txt",".nojekyll"]

rst_epilog = """
.. |project| replace:: {project}
.. |project_sub| replace:: {project_sub}
""".format(project=project, project_sub=project_sub)

