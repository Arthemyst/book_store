# book_store

## Introduction

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Arthemyst/book_store.git
$ cd book_store
```

This project requires Python 3.6 or later.

Create a virtual environment and activate it:

Linux:
```sh
$ python3 -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
(env)$ pip install -r requirements-dev.txt
```


Create a .env file in project root directory. The file format can be understood from the example below:
```sh
DEBUG=True
SECRET_KEY=your-secret-key # generate your own secret key
SQLITE_URL=sqlite:///my-local-sqlite.db
ALLOWED_HOSTS=127.0.0.1
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd src
(env)$ python3 manage.py runserver
```

To test applications:

```sh
(env)$ python3 -m pytest bookstore/tests/test_book_import.py
```