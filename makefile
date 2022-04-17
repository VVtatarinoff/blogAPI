install:
	poetry install

tests:
	poetry run pytest --verbose


coverage:
	poetry run pytest --cov=comments_api

build:
	poetry build
run:
	poetry run python manage.py runserver

log:
	heroku logs --tail

lint:
	poetry run flake8

.PHONY: install  build run tests log lint translate