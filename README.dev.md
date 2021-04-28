# `notebooks` developer documentation

If you're looking for user documentation, go [here](README.md).

## Development install

```shell
# Create a virtual environment, e.g. with
python3 -m venv env

# activate virtual environment
source env/bin/activate

# make sure to have a recent version of pip and setuptools
python3 -m pip install --upgrade pip setuptools

# (from the project root directory)
# install notebooks as an editable package
python3 -m pip install --no-cache-dir --editable .
# install development dependencies
python3 -m pip install --no-cache-dir --editable .[dev]
```

Afterwards check that the install directory is present in the `PATH` environment variable.

## Running the tests

Running the tests requires an activated virtual environment with the development tools installed.

```shell
# unit tests
pytest
pytest tests/
```

## Running linters locally

For linting we will use [prospector](https://pypi.org/project/prospector/) and to sort imports we will use
[isort](https://pycqa.github.io/isort/). Running the linters requires an activated virtual environment with the
development tools installed.

```shell
# linter
prospector

# recursively check import style for the notebooks module only
isort --recursive --check-only notebooks

# recursively check import style for the notebooks module only and show
# any proposed changes as a diff
isort --recursive --check-only --diff notebooks

# recursively fix import style for the notebooks module only
isort --recursive notebooks
```

You can enable automatic linting with `prospector` and `isort` on commit by enabling the git hook from `.githooks/pre-commit`, like so:

```shell
git config --local core.hooksPath .githooks
```

## Generating the API docs

```shell
cd docs
make html
```

The documentation will be in `docs/_build/`

## Versioning

Bumping the version across all files is done with bumpversion, e.g.

```shell
bumpversion major
bumpversion minor
bumpversion patch
```

## Making a release

This section describes how to make a release in 3 parts:

1. preparation
1. making a release on PyPI
1. making a release on GitHub

### (1/3) Preparation

1.  Update the `CHANGELOG.md`
2.  Verify that the information in `CITATION.cff` is correct, and that `.zenodo.json` contains equivalent data
3.  Make sure the version has been updated.
4.  Run the unit tests with `pytest tests/`

### (2/3) PyPI

In a new terminal, without an activated virtual environment or an env directory:

```shell
# prepare a new directory
cd $(mktemp -d --tmpdir notebooks.XXXXXX)

# fresh git clone ensures the release has the state of origin/main branch
git clone https://github.com/puregome/notebooks .

# prepare a clean virtual environment and activate it
python3 -m venv env
source env/bin/activate

# make sure to have a recent version of pip and setuptools
python3 -m pip install --upgrade pip setuptools

# install runtime dependencies and publishing dependencies
python3 -m pip install --no-cache-dir .
python3 -m pip install --no-cache-dir .[publishing]

# clean up any previously generated artefacts 
rm -rf notebooks.egg-info
rm -rf dist

# create the source distribution and the wheel
python3 setup.py sdist bdist_wheel

# upload to test pypi instance (requires credentials)
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Visit
[https://test.pypi.org/project/notebooks](https://test.pypi.org/project/notebooks)
and verify that your package was uploaded successfully. Keep the terminal open, we'll need it later.

In a new terminal, without an activated virtual environment or an env directory:

```shell
cd $(mktemp -d --tmpdir notebooks-test.XXXXXX)

# prepare a clean virtual environment and activate it
python3 -m venv env
source env/bin/activate

# make sure to have a recent version of pip and setuptools
pip install --upgrade pip setuptools

# install from test pypi instance:
python3 -m pip -v install --no-cache-dir \
--index-url https://test.pypi.org/simple/ \
--extra-index-url https://pypi.org/simple notebooks
```

Check that the package works as it should when installed from pypitest.

Then upload to pypi.org with:

```shell
# Back to the first terminal,
# FINAL STEP: upload to PyPI (requires credentials)
twine upload dist/*
```

### (3/3) GitHub

Don't forget to also make a release on GitHub. If your repository uses the GitHub-Zenodo integration this will also
trigger Zenodo into making a snapshot of your repository and sticking a DOI on it.
