# FastAPI Example - Шаблон проектирования DDD

## Стэк
 - [Python 3.10](https://www.python.org/downloads/release/python-3100/)
 - [FastAPI](https://fastapi.tiangolo.com)
 - [SQLAlchemy](https://www.sqlalchemy.org)
   - [Postgres](https://www.postgresql.org)
 - [Docker](https://www.docker.com)
   - [Docker Compose](https://docs.docker.com/compose/)
 - [Poetry](https://python-poetry.org)

## Переменные окружения
.env file
   - POSTGRES_USER - database root name
   - POSTGRES_PASSWORD - database root password
   - DB_HOST - database's hostname
   - DB_PORT - database's port
   - DB_NAME - database's name
   - DB_USER - database's username
   - DB_PASS - database user's password
   - PORT - port which will be listening for incoming connections

## Структура

```tree
├── core
├── app
│   ├── main.py
│   ├── dependencies.py
│   ├── config.py
│   └── features
│       └── users
│           ├── data
│           │   ├── repositories
│           │   │   ├── user_unit_of_work_impl.py
│           │   │   └── user_repository_impl.py
│           │   ├── services
│           │   │   └── user_query_service_impl.py
│           │   └── models
│           │       ├── user.py
│           │       └── database.py
│           ├── domain
│           │   ├── entities
│           │   │   ├── user_command_model.py
│           │   │   ├── user_common_model.py
│           │   │   ├── user_entity.py
│           │   │   └── user_query_model.py
│           │   ├── repositories
│           │   │   ├── user_repository.py
│           │   │   └── user_unit_of_work.py
│           │   ├── services
│           │   │   └── user_query_service.py
│           │   └── usecases
│           │       ├── create_user.py
│           │       ├── delete_user.py
│           │       ├── get_user.py
│           │       ├── get_users.py
│           │       └── update_user.py
│           ├── presentation
│           │   ├── routes
│           │   │   ├── __init__.py
│           │   │   ├── create_user_route.py
│           │   │   ├── delete_user_route.py
│           │   │   ├── get_user_route.py
│           │   │   ├── get_users_route.py
│           │   │   └── update_user_route.py
│           │   └── schema
│           │       └── routes
│           └── dependencies.py
└── tests
```

# Setup
1. Clone repository
2. Create .env file and setup env variables
3. Run `docker-compose up`
4. Access the API document `http://localhost:<specified_opened_port>`
