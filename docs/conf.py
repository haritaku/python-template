# -- Project information -----------------------------------------------------

project = ""
copyright = "2021, haritaku"
author = "haritaku"


# -- General configuration ---------------------------------------------------

extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinxcontrib.katex",
    "nbsphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# todo config
todo_include_todos = True

# napoleon config
napoleon_numpy_docstring = False
napoleon_use_ivar = True
napoleon_use_admonition_for_notes = True
napoleon_custom_sections = [("Returns", "params_style")]

# type hints config
autodoc_typehints = "description"
autodoc_member_order = "bysource"

# autosummary config
autosummary_generate = True

# recommonmark config
source_suffix = [".rst", ".md"]
source_parsers = {
    ".md": "recommonmark.parser.CommonMarkParser",
}

add_module_names = False
templates_path = ["_templates"]
language = "en"

exclude_patterns = ["README.md", "**.ipynb_checkpoints"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {"style_nav_header_background": "#03AF7A"}

html_static_path = ["_static"]

# html_css_files = ['custom.css']
