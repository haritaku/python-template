# -- Project information -----------------------------------------------------

project = ""
copyright = "2021, haritaku"
author = "haritaku"


# -- General configuration ---------------------------------------------------
# Built-in extensions: https://www.sphinx-doc.org/ja/master/usage/extensions/index.html
extensions = [
    "sphinx.ext.autodoc",  # https://www.sphinx-doc.org/ja/master/usage/extensions/autodoc.html
    "sphinx.ext.intersphinx",  # https://www.sphinx-doc.org/ja/master/usage/extensions/intersphinx.html
    "sphinx.ext.napoleon",  # https://www.sphinx-doc.org/ja/master/usage/extensions/napoleon.html
    "sphinx.ext.todo",  # https://www.sphinx-doc.org/ja/master/usage/extensions/todo.html
    "sphinx.ext.viewcode",  # https://www.sphinx-doc.org/ja/master/usage/extensions/viewcode.html
    "sphinx.ext.autosummary",  # https://www.sphinx-doc.org/ja/master/usage/extensions/autosummary.html
    "sphinx.ext.mathjax",  # https://www.sphinx-doc.org/ja/master/usage/extensions/math.html#module-sphinx.ext.mathjax
    "sphinxcontrib.katex",  # https://sphinxcontrib-katex.readthedocs.io/en/latest/
    "nbsphinx",  # https://nbsphinx.readthedocs.io/en/latest/
    "myst_parser",  # https://myst-parser.readthedocs.io/en/latest/index.html

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

add_module_names = False
templates_path = ["_templates"]
language = "en"

exclude_patterns = ["README.md", "**.ipynb_checkpoints"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {"style_nav_header_background": "#03AF7A"}

html_static_path = ["_static"]

# html_css_files = ['custom.css']
