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

Create a .env file in project root directory. The file format can be understood from the example below:
```sh
DEBUG=True
SECRET_KEY=your-secret-key # generate your own secret key
DATABASE_URL=psql://postgres:postgres@database:5432/postgres
ALLOWED_HOSTS=127.0.0.1,localhost
```

Application runs on docker. Please run docker-compose to install dependiences and run application:

```sh
$ docker-compose -f docker/docker-compose.yaml up --build
```
