# Fast API Boilerplate
REST API project template built with Fast API.
## Features
- SQLAlchemy ORM
- Alembic auto migration
- Base CRUD Class set
## How to run Server
```sh
# Copy .env.example
cp .env.example .env

# Run docker-compose
docker-compose up
```
## How To Use Migration
### How to Create Migration Script
```sh
alembic revision -m "create account table"
```
### How to Migrate Upgrade
```sh
alembic upgrade head
```
### How to Migrade Downgrade
```sh
alembic downgrade base
```
## Alembic Autogenerate
alembic autogenerate is now working fine. Just import the model you want to make autogenerate migration in __init__.py of models folder. Then run this command below.
```sh
alembic revision --autogenerate -m "Added price column"
```