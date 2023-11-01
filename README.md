# Airveda-Assignment

This is the submission for an assignment given by AirVeda.


## Run Locally

After installing the project zip file

Go to the project directory

```bash
  cd iotproject
```

Install dependencies

```bash
  pip install django
  pip install djangorestframework
  pip install matplotlib
```
Run migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```
Create a superuser to manage devices and readings

```bash
  python manage.py createsuperuser
```
Run the server

```bash
  python manage.py runserver
```


## Screenshots

List all devices or create new devices
