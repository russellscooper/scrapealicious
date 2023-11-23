import sys
import os

project = 'Scrapealicious'
copyright = '2023, Samuel R Cooper'
author = 'Samuel R Cooper'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

html_output_directory = os.path.join('..', '..')

html_extra_path = [html_output_directory]

templates_path = ['_templates']
sys.path.append(os.path.abspath('C:\\Users\\samco\\2023\\scrapealicious\\scrapealicious\\app'))

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.git']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
