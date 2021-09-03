# Best practices for a Python web application

## Linters
Linter is a tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs.\
Commonly used linters:

- [Pylint](https://github.com/PyCQA/pylint) - looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions
- [Bandit](https://github.com/PyCQA/bandit) - find common security issues in Python code.
- [Darglint](https://github.com/terrencepreilly/darglint) - checks whether a docstring's description matches the actual function/method implementation.

## Formatting tools
Code formatters changes your code to be clean and therefore improve readability. \
Commonly used formaters:
- [black](https://github.com/psf/black) - code formatting 
- [isort](https://github.com/PyCQA/isort) - import formatting 
- [pyupgrade](https://github.com/asottile/pyupgrade) -  automatically upgrades syntax for newer versions of the language.

## Static analysis 
- [Mypy](https://github.com/python/mypy/) - static type checker for python

## Framework 
- This simple web application created using [Flask](https://github.com/pallets/flask). \
It was choosen because it is simple and provide an ability to create apps quickly and effortlessly.

## Adding LICENSE
- [lice](https://github.com/licenses/lice)

## Create .gitignore

## Tests
- [pytest](https://github.com/pytest-dev/pytest/) - framework makes it easy to write small tests

The testing is done using `pytest` framework, since it:

- has fixture mechanism for state preparation
- provides easy interface for testing
- is a flexible framework allowing custom plugins and test parametrization

## Unit testing best practices

- Tests must be fully independent. In other words:

  - run on fresh data every time
  - do not have contraints on execution order

- Refactor code, so we can test one piece of functionality at a time

- Have small readable tests.

- If there are not a lot of tests, we can add running test into pre-commit hooks
  so that developers do not push a broken code

- Keep track of test coverage to verify that new code is at least covered by tests

- Unit tests should be fast in order not to slow down development.
  If there are slow test, they should be filtered out and run periodically in a CI job.


## List of other best practices

1. Follow guidelines from PEP 8 (Style Guide for Python Code)
2. Use already existing libraries from PyPI
3. Utilize `git` (or other VCS) for better version control
4. Separate files to appropriate folders and functions to appropriate modules
5. Use linter wherever possible
6. Follow the Zen of Python
7. Separate different projects into separate Virtual Environments
8. Use production ready and tested frameworks, such as Django or Flask
