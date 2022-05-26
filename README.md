# bookstore

## Introduction

Django-rest application used to manage bookstore. 
App uses database with books.
Books have parameters like:
- external id - id of a book from external source
- title - title of the book
- authors - list of the authors of the book
- acquired - false or true
- published year
- thumbnail - link 

App give possibility to import books from google api: 

Adress of import page: https://bookstore-pl-123.herokuapp.com/import/
What to do for import:
put in post field:
{"authors":"<surname of author>"} -> ex. {"authors":"Tolkien"}
If new books imported should be message: {"imported": <count of books>}

Check books:
Adress of check list of books page: https://bookstore-pl-123.herokuapp.com/books/
Is possibility to filter books by title, authors, published year (from specific year to specific year), if acquired)
Possible is to CREATE new book by choosing parameters.

Detail of specific book:
Adress to check specific book: https://bookstore-pl-123.herokuapp.com/books/<specific id> -> ex. https://bookstore-pl-123.herokuapp.com/books/2
Possible is to DELETE, PATCH (full or partial update) or PUT

Possible to check version of api:
https://bookstore-pl-123.herokuapp.com/api_spec

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
(env)$ pip install -r requirements-dev.txt
```


Create a .env file in src directory. The file format can be understood from the example below:
```sh
DEBUG=True
SECRET_KEY=your-secret-key # generate your own secret key
SQLITE_URL=sqlite:///my-local-sqlite.db
ALLOWED_HOSTS=127.0.0.1
```

```sh
(env)$ cd src
(env)$ python3 manage.py runserver
```

To test applications:

```sh
(env)$ cd src
(env)$ python3 -m pytest bookstore/tests/test_book_import.py
```