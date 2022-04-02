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
