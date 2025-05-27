Library Manager CLI

Library Manager CLI is a command-line interface application that allows users to manage authors and books using an SQLite database. It uses SQLAlchemy ORM for database interactions.

Features

View all authors and books

Add new authors and books

Delete authors and books

Find authors and books by ID

View books written by a specific author

Technologies Used

Python 3.8+

SQLAlchemy

Alembic

Pipenv

File Structure

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py          # CLI interface logic
    ├── db
    │   ├── models.py   # SQLAlchemy models for Author and Book
    │   ├── seed.py     # Seed script to populate the database
    │   └── migrations  # Alembic migrations folder
    └── helpers.py      # Helper functions (optional)

How to Run the Project

Clone the repository

Navigate to the project directory

Run pipenv install

Activate the environment with pipenv shell

Set up the database:

Run alembic upgrade head to apply migrations

Run python -m lib.db.seed to populate initial data

Start the CLI:

Run python lib/cli.py

Sample Usage

Library Manager
1. View all authors
2. View all books
3. Add a new author
...
Enter your choice:

Models

Author

id: Integer, Primary Key

name: String

books: Relationship to Book

Book

id: Integer, Primary Key

title: String

author_id: Foreign Key to Author

Functions Summary

Author Methods

create(session, name)

delete(session, author)

get_all(session)

find_by_id(session, id)

Book Methods

create(session, title, author_id)

delete(session, book)

get_all(session)

find_by_id(session, id)

Author

Created by Luke Kiprop as a Phase 3 Project.

