#!/usr/bin/env python
"""Setup script to make Cheshire installable with pip."""

from pathlib import Path

from setuptools import find_packages, setup

readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text()


setup(
    # This should be the *installed* package name e.g. catalystcoop.pudl not pudl
    name="catalystcoop.handbook",
    description="A one line description of the package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # setuptools_scm lets us automagically get package version from GitHub tags
    use_scm_version=True,
    author="Catalyst Cooperative",
    author_email="pudl@catalyst.coop",
    maintainer="Catalyst Cooperative Members",
    maintainer_email="pudl@catalyst.coop",
    url="https://catalystcoop-handbook.readthedocs.io",  # Can be repo or docs URL if no separate web page exists.
    project_urls={
        "Source": "https://github.com/catalyst-cooperative/handbook",
        "Documentation": "https://catalystcoop-handbook.readthedocs.io",
        "Issue Tracker": "https://github.com/catalyst-cooperative/handbook/issues",
    },
    license="MIT",
    # Fill in search keywords that users might use to find the package
    keywords=[],
    python_requires=">=3.10,<3.12",
    # In order for the dependabot to update versions, they must be listed here.
    # Use the format pkg_name>=x,<y", Included packages are just examples:
    install_requires=[
        "doc8>=0.9,<1.2",  # Ensures clean documentation formatting
        "furo>=2022.4.7",
        "myst-parser>=0.18,<2.1",
        "mdformat~=0.7.16",
        "mdformat-myst~=0.1.5",
        "sphinx>=4,!=5.1.0,<7.2.7",  # The default Python documentation engine
        "sphinx-autoapi>=1.8,<3.1",  # Generates documentation from docstrings
        "sphinx-issues>=1.2,<4.2",  # Allows references to GitHub issues
        "tox>=3.20,<4.15",  # Python test environment manager
        "pre-commit>=2.9,<3.8",  # Allow us to run pre-commit hooks in testing
        "pydocstyle>=5.1,<6.4",  # Style guidelines for Python documentation
    ],
    # A controlled vocabulary of tags used by the Python Package Index.
    # Make sure the license and python versions are consistent with other arguments.
    # The full list of recognized classifiers is here: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    # Directory to search recursively for __init__.py files defining Python packages
    packages=find_packages("src"),
    # Location of the "root" package:
    package_dir={"": "src"},
    # package_data is data that is deployed within the python package on the
    # user's system. setuptools will get whatever is listed in MANIFEST.in
    include_package_data=True,
)
