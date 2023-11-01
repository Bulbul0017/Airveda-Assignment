# Airveda-Assignment

This is the submission for an assignment given by Airveda.


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
![Screenshot 1](https://github.com/Bulbul0017/Airveda-Assignment/assets/74949576/9c8ecfbb-cd1e-455e-bbd4-1ae994e2bd1d)

Retrieve or delete a device instance
![Screenshot 2](https://github.com/Bulbul0017/Airveda-Assignment/assets/74949576/99138f6e-db36-4492-8093-8b1d977e3165)

Device graph



