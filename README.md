# retail-chain
Retail Chain Application for study the Django Framework.

## Make the development environment (Tested on Ubuntu 18.04 with Python 3.6.9)

1. Create the virtual environment:
```sh
$ cd retail-chain/source
$ python3 -m venv venv
```
2. Initialize the venv, upgrade pip and installer the project dependencies:
```sh
$ source venv/bin/activate
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```
3. Create the SQLite3 database, create and running migrations:
```sh
$ python manage.py migrate
$ python manage.py makemigrations webapp
$ python manage.py migrate webapp
```
4. Create your admin account:
```sh
$ python manage.py createsuperuser
```
5. Run the project:
```sh
$ python manage.py runserver
```
6. Access the admin panel to try the models: http://127.0.0.1:8000/admin

> To see or manage the SQLite3 database its recommended to use the SQLite Studio:
https://github.com/pawelsalawa/sqlitestudio/releases/tag/3.2.1
