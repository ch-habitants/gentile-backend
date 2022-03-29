# Getting started

To prepare your python environment to work on `gentile-backend`, you will need to
install the dependencies. You can do this by running

```
pip install -r requirements.txt -r requirements-dev.txt
```

Before being merged into the project, the code must satisfy the automatic checks.
Before pushing to the repository, please run the following checks locally:

```
flake8 gentile --count --show-source --statistics
mypy gentile --strict --non-interactive --pretty
```

You can also run the command

```
pre-commit install
```

once, and have them run automatically on every commit.
