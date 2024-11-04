# TodoAPI

A Django REST API application for managing a basic todo list.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete todo items.
- **Token-Based Authentication**: Secure the API using Django Rest Framework's `TokenAuthentication`.
- **Filtering**: Query todo items based on title.
- **Testing**: Comprehensive tests for all API endpoints using Django's testing framework.

## Requirements

- Python 3.12
- Django
- Django Rest Framework
- Django Rest Framework Simple JWT

## Installation

1. **Clone the Repository**

   ```sh
   git clone <repository-url>
   cd TodoAPI

2. Create a Virtual Environment
    - python3.12 -m venv venv
    - source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies
    - using Pipfile:
        + pip install pipenv
        + pipenv install

4. Apply Migrations
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
    - python manage.py test


