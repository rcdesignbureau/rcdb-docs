import datetime as dt
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RC Design Bureau'
copyright = f"{dt.datetime.now().strftime('%Y')}, RC Design Bureau" # Updates the copyright to the current year
author = "Alessandro Bonecchi, Antonio O'Hara, Eddie O'Hara"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
templates_path = ['_templates']
exclude_patterns = []
language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_logo = 'assets/logo.png'
html_favicon = 'assets/favicon.ico'

# -- Options for LaTeX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
latex_engine = 'pdflatex'
latex_documents = [('index_latex', 'rcdb-docs.tex', 'RC Design Bureau Documentation', "Alessandro Bonecchi, Antonio O'Hara, and Eddie O'Hara", 'manual', False)]
latex_elements = {
    'documentclass': 'article',
    'papersize': 'letterpaper',
    'extraclassoptions': 'openany'
}
