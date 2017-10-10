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

### License: MIT