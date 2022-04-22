# REST API для системы комментариев блога

Тестовое задание, текст которого размещен в файле task.txt

## docker
Инструкция для docker размещена в файле README.md в папке docker/

## Запуск локально:
Для того, чтобы запустить проект необходимо после скачивания репозитария:
    1. Создать базу данных postgres
    2. Создать файл .env в корне проекта, где нужно указать следующие константы (пример)
        SECRET_KEY='your secret here there'
        ENGINE='django.db.backends.postgresql_psycopg2'
        DB_NAME='blog_db'
        USER='vlad'
        PASSWORD='password'
        HOST='localhost'
        PORT=''
        DEBUG=True
        DATABASE_URL=postgres://vlad:password@localhost/blog_db
    3. Создать таблицы в бд с помощью команды
            python manage.py migrate
    4. Доуступна админ-панель (/admin/), для этого нужно создать суперпользователя
            python manage.py createsuperuser
    5. Запустить сервер
            python manage.py runserver

## Endpoints можно просмотреть на странице /swagger/

Стэк использованных технологий:

    - django rest framework
    - mptt-django 
    - postgres
    - flake8
    - poetry
    - drf-yasg
    
    