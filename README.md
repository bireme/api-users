# Setup ambiente local

## Virtualenv

    $ poetry new
    $ poetry add djando
    $ poetry shell

## Django project

    $ mkdir app
    $ django-admin startproject api-users app
    $ python manage.py startapp users
    $ python manage.py migrate
    $ python manage.py createsuperuser
