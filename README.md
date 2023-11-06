# fastapi-beanie-jwt

[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sample FastAPI server with JWT auth and Beanie ODM

## Intro

This starter app provides a basic account API on top of a [MongoDB]() store with the following features:

- Registration
- Email verification
- Password reset
- JWT auth login and refresh
- User model CRUD

It's built on top of these libraries to provide those features:

- [FastAPI]() - Python async micro framework built on [Starlette]() and [PyDantic]()
- [Beanie ODM]() - Async [MongoDB]() object-document mapper built on [PyDantic]()
- [fastapi-jwt]() - JWT auth for [FastAPI]()
- [fastapi-mail]() - Mail server manager for [FastAPI]()

## Setup

This codebase was written for Python 3.11 and above. Don't forget about a venv as well. The `python` commands below assume you're pointing to your desired Python3 target.

First we'll need to install our requirements.

```bash
python -m pip install -e .
```

Before we run the server, there is one config variable you'll need to generate the password salt. To do this, just run the script in this repo.

```bash
python gen_salt.py
```

There are other settings in `config.py` and the included `.env` file. Assuming you've changed the SALT value, everything should run as-is if there is a local [MongoDB]() instance running ([see below](#test) for a Docker solution). Any email links will be printed to the console by default.

## Run

This sample uses [uvicorn]() as our ASGI web server. This allows us to run our server code in a much more robust and configurable environment than the development server. For example, ASGI servers let you run multiple workers that recycle themselves after a set amount of time or number of requests.

```bash
uvicorn myserver.main:app --reload --port 8080
```

You're API should now be available at http://localhost:8080

## Develop

This codebase is uses [mypy]() for type checking and [ruff]() for everything else. Install both with the dev tag.

```bash
python -m pip install -e .[dev]
```

To run the type checker:

```bash
mypy myserver
```

To run the linter and code formatter:

```bash
ruff check myserver
ruff format myserver
```

## Test

The sample app also comes with a test suite to get you started.

Make sure to install the requirements found in the test folder before trying to run the tests.

```bash
python -m pip install -e .[test]
```

The tests need access to a [MongoDB]() store that is emptied at the end of each test. The easiest way to do this is to run a Mongo container in the background.

```bash
docker run -d -p 27017:27017 mongo:7
```

You can also connect to a remote server if you're running tests in a CI/CD pipeline. Just set the `TEST_MONGO_URI` in the environment. This value defaults to localhost and is only checked in the test suite. It should **never** use your `MONGO_URI`.

Then just run the test suite.

```bash
pytest
```

[MongoDB]: https://www.mongodb.com "MongoDB NoSQL homepage"
[FastAPI]: https://fastapi.tiangolo.com "FastAPI web framework"
[Beanie ODM]: https://roman-right.github.io/beanie/ "Beanie object-document mapper"
[Starlette]: https://www.starlette.io "Starlette web framework"
[PyDantic]: https://pydantic-docs.helpmanual.io "PyDantic model validation"
[fastapi-jwt]: https://github.com/k4black/fastapi-jwt "JWT auth for FastAPI"
[fastapi-mail]: https://github.com/sabuhish/fastapi-mail "FastAPI mail server"
[uvicorn]: https://www.uvicorn.org "Uvicorn ASGI web server"
[mypy]: https://www.mypy-lang.org "mypy Python type checker"
[ruff]: https://docs.astral.sh/ruff/ "Ruff code linter and formatter"