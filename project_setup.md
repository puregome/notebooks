# Project Setup

Here we provide some details about the project setup. Most of the choices are explained in the
[guide](https://guide.esciencecenter.nl). Links to the relevant sections are included below. Feel free to remove this
text when the development of the software package takes off.

For a quick reference on software development, we refer to [the software guide
checklist](https://guide.esciencecenter.nl/#/best_practices/checklist).

## Version control

Once your Python package is created, put it under [version
control](https://guide.esciencecenter.nl/#/best_practices/version_control)! We recommend using
[git](http://git-scm.com/) and [github](https://github.com/).

```shell
cd notebooks
git init
git add --all
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/puregome/notebooks
```

Go to
[https://github.com/puregome?tab=repositories](https://github.com/puregome?tab=repositories)
and create a new repository named notebooks as an empty repository, then:

```shell
git push --set-upstream origin main
```

## Python versions

This repository is set up with Python versions:

- 3.6
- 3.7
- 3.8
- 3.9

Add or remove Python versions based on project requirements. See [the
guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python) for more information about Python
versions.

## Package management and dependencies

You can use either pip or conda for installing dependencies and package management. This repository does not force you
to use one or the other, as project requirements differ. For advice on what to use, please check [the relevant section
of the
guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=dependencies-and-package-management).

- Runtime dependencies should be added to `setup.cfg` in the `install_requires` list under `[options]`.
- Development dependencies should be added to `setup.cfg` in one of the lists under `[options.extras_require]`.

## Packaging/One command install

You can distribute your code using PyPI.
[The guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=building-and-packaging-code) can
help you decide which tool to use for packaging.

## Testing and code coverage

- Tests should be put in the `tests` folder.
- The `tests` folder contains:
  - Example tests that you should replace with your own meaningful tests (file: `test_my_module.py`)
- The testing framework used is [PyTest](https://pytest.org)
  - [PyTest introduction](http://pythontesting.net/framework/pytest/pytest-introduction/)
  - PyTest is listed as a development dependency, and can thus be installed with `pip3 install --editable .[dev]`
- Tests can be run with `pytest`
  - This is configured in `setup.cfg`
- The project uses [GitHub action workflows](https://docs.github.com/en/actions) to automatically run tests on GitHub infrastructure against multiple Python versions
  - Workflows can be found in [`.github/workflows`](.github/workflows/)
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=testing)

## Documentation

- Documentation should be put in the [`docs/`](docs/) directory. The contents have been generated using `sphinx-quickstart` (Sphinx version 1.6.5).
- We recommend writing the documentation using Restructured Text (reST) and Google style docstrings.
  - [Restructured Text (reST) and Sphinx CheatSheet](http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html)
  - [Google style docstring examples](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- The documentation is set up with the ReadTheDocs Sphinx theme.
  - Check out its [configuration options](https://sphinx-rtd-theme.readthedocs.io/en/latest/).
- To generate HTML documentation, run `make html` in the `docs/` folder.
- To put the documentation on [ReadTheDocs](https://readthedocs.org), log in to your ReadTheDocs account, and import
  the repository (under 'My Projects').
  - Include the link to the documentation in your project's [README.md](README.md).
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=writingdocumentation)

## Coding style conventions and code quality

- Check your code style with `prospector`
- You may need run `pip install --editable .[dev]` first, to install the required dependencies
- You can use `yapf` to fix the readability of your code style and `isort` to format and group your imports
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=coding-style-conventions)

## Continuous code quality

- [Sonarcloud](https://sonarcloud.io/) is used to perform quality analysis and code coverage report on each push
- Sonarcloud must be configured for the analysis to work
  1. go to [Sonarcloud](https://sonarcloud.io/projects/create)
  2. login with your GitHub account
  3. add organization or reuse existing one
  4. set up repository
  5. go to [new code definition administration page](https://sonarcloud.io/project/new_code?id=puregome_notebooks) and select `Number of days` option
- The analysis will be run by [GitHub Action workflow](.github/workflows/sonarcloud.yml)
- To be able to run the analysis, a token must be created at [Sonarcloud account](https://sonarcloud.io/account/security/) and this token must be added as `SONAR_TOKEN` to [secrets on GitHub](https://github.com/puregome/notebooks/settings/secrets/actions)

## Package version number

- We recommend using [semantic versioning](https://guide.esciencecenter.nl/#/best_practices/releases?id=semantic-versioning).
- For convenience, the package version is stored in a single place: `notebooks/.bumpversion.cfg`.
  For updating the version number, make sure the dev dependencies are installed and run `bumpversion patch`,
  `bumpversion minor`, or `bumpversion major` as appropriate.
- Don't forget to update the version number before [making a release](https://guide.esciencecenter.nl/#/best_practices/releases)!

## Publish on Python Package Index (PyPI)

To publish your package on PyPI, you need to create a [PyPI API token](https://pypi.org/help#apitoken) and
save it as a secret called `PYPI_TOKEN` on [Settings page](https://github.com/puregome/notebooks/settings/secrets/actions)

[Creating a release](https://github.com/puregome/notebooks/releases/new) on GitHub will trigger a [GitHub action workflow](.github/workflows/publish.yml) to publish the release on PyPI for you.

## Logging

- We recommend using the logging module for getting useful information from your module (instead of using print).
- The project is set up with a logging example.
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=logging)

## CHANGELOG.md

- Document changes to your software package
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/releases?id=changelogmd)

## CITATION.cff

- To allow others to cite your software, add a `CITATION.cff` file
- It only makes sense to do this once there is something to cite (e.g., a software release with a DOI).
- Follow the [making software citable](https://guide.esciencecenter.nl/#/citable_software/making_software_citable) section in the guide.

## CODE_OF_CONDUCT.md

- Information about how to behave professionally
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/documentation?id=code-of-conduct)

## CONTRIBUTING.md

- Information about how to contribute to this software package
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/documentation?id=contribution-guidelines)

## MANIFEST.in

- List non-Python files that should be included in a source distribution
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=building-and-packaging-code)

## NOTICE

- List of attributions of this project and Apache-license dependencies
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/licensing?id=notice)
