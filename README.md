# fastapi-beanie-jwt
Sample FastAPI server with JWT auth and Beanie ODM

## Setup

First we'll need to install our requirements:

```bash
pip install -r requirements.txt
```

Before we run the server, there is one config variable you'll need to generate the password salt. To do this, just run the script in this repo.

```bash
python gen_salt.py
```

## Run

```bash
uvicorn myserver.main:app --reload --port 8080
```

## Test

Make sure to install the requirements found in the test folder before trying to run the tests.

The tests need access to a Mongo service. The easiest way to do this is to run a Mongo container in the background:

```bash
docker run -d mongo
```

Then jsut run the test suite

```bash
pytest
```
