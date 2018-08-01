# Brocante

A web application to manage Flea Markets in small communities. It is intended to gather people from a community in a
physical space to sell their unused items to other people that might find those items useful.

## Features

- Registration form to allow people to request one or more slots in the flea market.
- Email automatically sent to the user when the registration is finished.
- Confirmation of request of reservation by email.
- Assignment of a reservation to a slot and details of the assignment sent by email.
- Management of slots available.
- Statistics of the ocupation.
- Management of a waiting list.

## How to Use

This project uses the stack Python 3.5 / Django 1.11 / PostgreSQL 9.6.

To use this project, follow these steps:

### Create your working environment

Create the database and the necessary permissions:

    $ createdb brocante
    $ createuser brocante_usr -P
    $ psql -d brocante
      # grant connect on database brocante to brocante_usr;
      # revoke connect on database brocante from public;
      # alter user brocante_usr createdb;
      # \q
      
Clone the project locally from GitHub:

    $ mkdir -R ~/python/projects
    $ cd ~/python/projects
    $ git clone https://github.com/htmfilho/brocante.git
    
Create a Python virtual environment:
    
    $ cd brocante
    $ python3 -m venv venv
    $ source venv/bin/activate
    
Install the dependencies:

    [venv] $ pip install -r requirements.txt
    
Set the environment variables in the file .env:

    cp .env.example .env
    
The following variables must be defined:

    SECRET_KEY = ''
    RECAPTCHA_PUBLIC_KEY = ''
    RECAPTCHA_SECRET_KEY = ''
    EMAIL_USE_SSL = True
    EMAIL_HOST = ''
    EMAIL_PORT = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    
Initialize the database and create a super user for the application:

    [venv] $ ./manage.py migrate
    [venv] $ ./manage.py createsuperuser

Run the server:    

    [venv] $ ./manage.py runserver

Visit the address http://localhost:8000 to view the registration form, and 
http://localhost:8000/admin for the administration console.

### License: MIT