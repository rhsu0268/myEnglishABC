# myEnglishABC

# Project Setup

Create a new virtualenv for best practice. 

```
python3 -m venv <Name of virtualenv>
```

Start the virtualenv: 

```
source <Name of virtualenv>/bin/activate
```

To stop:

```
deactivate
```

Here are steps to create a new django application:

Start up your virtualenv. 

Install django with the following:

```
pip3 install django
```

Change into the root of the project directory and run:

```
python manage.py runserver 0.0.0.0:8000
```

To add an application to the project:

```
python manager.py startapp <name of app>
```

Setting up mySQL:

1. Install python-mysql

For Python 3:

```
pip install PyMySQL
```

2. 

