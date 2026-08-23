# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

# SRC_DIR = Path(__file__).resolve().parents[2] / "src"
# sys.path.insert(0, str(SRC_DIR))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Churn Prediction"
copyright = "2026, alexandrebsc, brendonbachie, gabscor, GrazielleNascimento, juliomj"
author = "alexandrebsc, brendonbachie, gabscor, GrazielleNascimento, juliomj"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}

templates_path = ["_templates"]
exclude_patterns = []

language = "pt"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
