import datetime as dt
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RC Design Bureau'
copyright = f"{dt.datetime.now().strftime('%Y')}, RC Design Bureau" # Updates the copyright to the current year
author = "Alessandro Bonecchi, Antonio O'Hara, Eddie O'Hara, and Johann Webber at RC Design Bureau"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_logo = 'assets/logo.png'
html_favicon = 'assets/favicon.ico'
