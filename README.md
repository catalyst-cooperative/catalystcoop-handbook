# Catalyst Cooperative Handbook

[The Catalyst Cooperative Handbook](https://catalystcoop-handbook.readthedocs.io/en/latest/) contains the cooperative's bylaws, policies and general information.

This repo allows us to version control and review changes to our policies.

<!-- readme-intro -->

## Setup Conda Environment

To edit these docs you need to clone the [`catalyst-handbook`](https://github.com/catalyst-cooperative/catalystcoop-handbook) repo and set up a conda environment:

```
git clone git@github.com:catalyst-cooperative/catalystcoop-handbook.git
```

We use the conda package manager to specify and update our development environment. We recommend using [miniconda](https://docs.conda.io/en/latest/miniconda.html) rather than the large pre-defined collection of scientific packages bundled together in the Anaconda Python distribution. You may also want to consider using [mamba](https://github.com/mamba-org/mamba) – a faster drop-in replacement for conda written in C++.

```
conda update conda
conda env create --name handbook --file environment.yml
conda activate handbook
```

## Git Pre-commit Hooks

Git hooks let you automatically run scripts at various points as you manage your source code. “Pre-commit” hook scripts are run when you try to make a new commit. These scripts can review your code and identify bugs, formatting errors, bad coding habits, and other issues before the code gets checked in. This gives you the opportunity to fix those issues before publishing them.

To make sure they are run before you commit any code, you need to enable the pre-commit hooks scripts with this command:

```
pre-commit install
```

The scripts that run are configured in the .pre-commit-config.yaml file.

## How to make changes

To make changes to the handbook, edit the relevant markdown documents in the `docs/` directory. Once the changes are made
you can build the docs by running:

```
tox -e docs
```

This command will build the docs and write the html files to `docs/_build/`. You can view the docs locally by opening the `docs/_build/index.html` file.
Once the docs are built locally, you can push your changes and open a PR for review. There is a GitHub Action that will build and deploy the changes
to Read the Docs.
