# Electronic Retail
Simple API for retail network
***
## Features
- User Registration/Login
- API
  - Creating/changing/deleting Units
  - Filter unit by country
- Django Admin
    - Creating/changing/deleting users
    - Creating/changing/deleting units
    - Creating/changing/deleting products
    - Creating/changing/deleting contacts
    - Filter unit by city

***
## Technology stack
- Python 3.10.6
- Django 4.2.1
- Django REST Framework 3.14.0
- Poetry 1.4.1
- django-environ = 0.10.0
- django-filter = 23.2
- djoser = 2.2.0
- djangorestframework-simplejwt = 5.2.2
- drf-spectacular = 0.26.2
- PostgreSQL
- Docker
- Docker-compose
- pre-commit
- black
- mypy
***
## Start app
1. Create .env file:
   ```
   SECRET_KEY=
   DEBUG=True
   DATABASE_URL=

   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_DB=
   POSTGRES_HOST=
2. Run docker container with database
   ```
    docker-compose up
***
## Project structure
- `core/`: login/register application
- `sales_network/`: network application
- `electronic_retail/`: Django settings
- `.env`: environment variables
- `.pre-commit-config.yaml`: pre-commit settings
- `docker-compose.yaml`: docker compose file
- `poetry.lock`: packages dependencies
- `pyproject.toml`: packages list
- `manage.py`: Django app management
