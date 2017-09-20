# Brocante

A web application to manage Flea Markets in small communities. It is intended to gather people from a community in a
physical space to sell their unused items to other people that might find those items useful.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment.

## How to Use

This project uses the stack Python 3.5 / Django 1.11 / PostgreSQL 9.6.

To use this project, follow these steps:

### Create your working environment

    $ createdb brocante
    $ createdb brocante_usr -P
    $ psql -d brocante
      # grant connect on database brocante to brocante_usr;
      # revoke connect on database brocante from public;
      # alter user brocante_usr createdb;
      # \q

    $ mkdir -R ~/python/projects
    $ cd ~/python/projects
    $ git clone https://github.com/htmfilho/brocante.git
    $ cd brocante
    $ virtualenv --python=python3.5 venv
    $ source venv/bin/activate

    [venv] $ pip install -r requirements.txt
    [venv] $ ./manage.py migrate
    [venv] $ ./manage.py createsuperuser
    [venv] $ ./manage.py runserver

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

### Translation Files

    $ brew install gettext
    $ brew upgrade gettext
    $ echo 'export PATH="/usr/local/opt/gettext/bin:$PATH"' >> ~/.bash_profile
    $ python manage.py makemessages
    $ python manage.py compilemessages
    $ heroku run python manage.py compilemessages


See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
