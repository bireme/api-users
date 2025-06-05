# Setup ambiente local

## Virtualenv

    $ uv init
    $ uv add djando

## Django project

    $ mkdir app
    $ django-admin startproject api-users app
    $ uv run manage.py startapp users
    $ uv run manage.py migrate
    $ uv run manage.py createsuperuser

## Local

    $ . ./set_env.sh
    $ uv sync
