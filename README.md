# Install Django

## Prerequire

- installed python
- installed pip

## Install

- Git: [Dijango](https://github.com/django/django.git)

### Latest version

```console
pip install Dijango
```

### Specific version

```console
pip install Django==1.11.29
```

## Check Django version

File: `version.py`

```python
import django

print(django.get_version())
```

Output:

```console
$ python version.py
1.11.29
```

## Create new project

Create project name `mysite`

```console
django-admin startproject mysite
```

Structure:

```console
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

## Run a server

Go to `mysite` and run command:

```console
python manage.py runserver
```

Default port 8000. Run server with other port

```console
python manage.py runserver 8080
```

## Create a web app

Create app name `polls`

```console
python manage.py startapp polls
```

Structure:

```console
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## Create views

When creating a view, need create an url as well

## Migration

It'll create table name base on `INSTALLED_APPS` in file `settings.py`

```console
python manage.py migrate
```

### Create new table

Declare tables in `INSTALLED_APPS` in file `settings.py` and run command

```console
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```console
python manage.py makemigrations polls
```

Run migrate:

```console
python manage.py migrate
```

## Work with table

```console
python manage.py shell
```

## Create new user

```console
python manage.py createsuperuser
```

## Keywords

- Dynamic URL
- Namespace URL
  - In template we can call `<namespace>:<name_url>`
- admin.TabularInline, admin.StackedInline
- Model
  - One-to-one OneToOneField
  - Many-to-one ForeignKey
  - Many-to-many ManyToManyField
  - Metadata
  - Inherit model
    - inherit abstract class
    - inherit multiple tables
    - inherit proxy class
