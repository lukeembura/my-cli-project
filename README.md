# Library Manager CLI

Library Manager CLI is a command-line interface application that allows users to manage authors and books using an SQLite database. It uses SQLAlchemy ORM for database interactions.

## Features

- **View all authors and books**: Displays a list of all authors and their books.
- **Add new authors and books**: Allows users to add new entries to the database.
- **Delete authors and books**: Removes entries from the database.
- **Find authors and books by ID**: Retrieves specific entries based on their ID.
- **View books written by a specific author**: Lists all books by a given author.

## Technologies Used

- Python 3.8+
- SQLAlchemy
- Alembic
- Pipenv

## File Structure

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py          # CLI interface logic
    ├── db
    │   ├── models.py   # SQLAlchemy models for Author and Book
    │   ├── seed.py     # Seed script to populate the database
 └── migrations  # Alembic migrations folder
    

## Prerequisites

- Python 3.8 or higher
- Pipenv installed (`pip install pipenv`)
- Alembic installed (`pip install alembic`)

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lukeembura/my-cli-project.git
   cd my-cli-project
   ```
2. Run `pipenv install`
3. Activate the environment with `pipenv shell`
4. Set up the database:
    - Run `alembic upgrade head` to apply migrations
    - Run `python -m lib.db.seed` to populate initial data
6. Start the CLI:
    - Run `python lib/cli.py`

## Sample Usage

```
Library Manager
1. View all authors
2. View all books
3. Add a new author
...
Enter your choice:
```

## Models

**Author**

- `id`: Integer, Primary Key
- `name`: String
- `books`: Relationship to Book

**Book**

- `id`: Integer, Primary Key
- `title`: String
- `author_id`: Foreign Key to Author

## Functions Summary

**Author Methods**

- `create(session, name)`
- `delete(session, author)`
- `get_all(session)`
- `find_by_id(session, id)`

**Book Methods**

- `create(session, title, author_id)`
- `delete(session, book)`
- `get_all(session)`
- `find_by_id(session, id)`

## Author

Created by Luke Kiprop as a Phase 3 Project.

