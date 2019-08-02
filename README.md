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

## How to Contribute

This project uses the stack Python / Django / PostgreSQL .

To use this project, follow these steps:

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
    
Create a Python virtual environment on Linux:
    
    $ cd brocante
    $ python3 -m venv venv
    $ source venv/bin/activate

or on Windows:

    $ cd brocante
    $ python -m venv venv
    $ venv\Scripts\activate
    
Install the dependencies:

    [venv] $ pip install -r requirements.txt
    
Create an .env file based on .env.example and set the environment variables:

    [venv] $ cp .env.example .env

On Windows, use the following command:

    [venv] $ copy .env.example .env
    
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

    [venv] $ python manage.py makemigrations
    [venv] $ python manage.py migrate
    [venv] $ python manage.py createsuperuser

[gettext] is required for the translation files. Make sure it's installed in your local machine. For Windows users, follow the instructions in the [Django documentation][gettext-windows]. Compiling translations:

    [venv] $ python manage.py makemessages -i venv
    [venv] $ python manage.py compilemessages

Run the server:    

    [venv] $ python manage.py runserver
    
Visit the address http://localhost:8000 to view the registration form, and 
http://localhost:8000/admin for the administration console.

### License: MIT

[gettext]: https://www.gnu.org/software/gettext/
[gettext-windows]: https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#gettext-on-windows