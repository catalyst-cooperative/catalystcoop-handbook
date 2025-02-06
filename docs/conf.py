"""Configuration file for the Sphinx documentation builder."""
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import datetime
import shutil
from pathlib import Path

import importlib
from sphinx.application import Sphinx

DOCS_DIR = Path(__file__).parent.resolve()

# -- Path setup --------------------------------------------------------------
# We are building and installing the pudl package in order to get access to
# the distribution metadata, including an automatically generated version
# number via importlib.metadata.version() so we need more than just an
# importable path.

# The full version, including alpha/beta/rc tags
release = importlib.metadata.version("catalystcoop.handbook")

# -- Project information -----------------------------------------------------

project = "Catalyst Cooperative Policy Handbook"
copyright = (  # noqa: A001
    f"2017-{datetime.date.today().year}, Catalyst Cooperative, CC-BY-4.0"
)
author = "Catalyst Cooperative"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_issues",
    "myst_parser",
]
todo_include_todos = True

myst_enable_extensions = [
    "substitution",
]

myst_substitutions = {
    "healthcare_stipend": 175,
    "tech_stipend": 3400,
    "cat_meetup_stipend": 230,
    "solo401k_match": 0.15,
    "solo401k_employee_max": 23_500,  # Update with info from this site: https://www.irs.gov/retirement-plans/one-participant-401k-plans
    "solo401k_employee_max_over_50": 31_000,
    "solo401k_total_max": 70_000,
    "current_year": 2025,
}

# GitHub repo
issues_github_path = "catalyst-cooperative/handbook"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
master_doc = "index"
html_theme = "furo"
html_logo = "_static/catalyst_logo-200x200.png"
html_icon = "_static/favicon.ico"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "navigation_with_keys": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Custom build operations -------------------------------------------------
def cleanup_rsts(app: Sphinx, exception: Exception) -> None:
    """Remove generated RST files when the build is finished."""
    (DOCS_DIR / "path/to/temporary/rst/file.rst").unlink()


def cleanup_csv_dir(app: Sphinx, exception: Exception) -> None:
    """Remove generated CSV files when the build is finished."""
    csv_dir = DOCS_DIR / "path/to/temporary/csv/dir/"
    if csv_dir.exists() and csv_dir.is_dir():
        shutil.rmtree(csv_dir)


def setup(app: Sphinx) -> None:
    """Add custom CSS defined in _static/custom.css."""
    app.add_css_file("custom.css")
    # Examples of custom docs build steps:
    # app.connect("build-finished", cleanup_rsts)
    # app.connect("build-finished", cleanup_csv_dir)
