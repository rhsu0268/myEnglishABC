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
python manage.py startapp <name of app>
```

## Setting up/Installing mySQL:

You need to install mysql on your computer. Here are some steps for mac users:

1. Install mysql from the oracle website.
2. Start up mysql:

```
sudo /usr/local/mysql/support-files/mysql.server start
```

3. Change the path variable.

```
nano ~/.bash_profile or nano ~/.profile
```

Add this line:PATH=/usr/local/mysql/bin:$PATH

4. Change your directory.

```
cd /usr/local/mysql
```

5. Run the following:

```
mysql -u root -p
```

It will prompt for the password you got from installation.

6. Set the password to something more secure/personal.

```
SET PASSWORD = PASSWORD('xxxxxx');
```

## Setting up MySQL with django


1. Go into settings.py and set the following:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<NAME OF DATABASE>',
        'USER': 'root',
        'PASSWORD': 'xxx',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }

}
```

2. Run the migrate command to sync mySQL with django:

```
python manage.py migrate
```

3. Then, go into mySQLPro:

Name:
Host: 127.0.0.1
USername: root
Password: <xxx>
database: Name of the database>
Port: 3306

Login to see your tables.

Here are 3 steps when you work with databases:

1. Change your models in models.py.
2. Run ```python manage.py makemigrations``` to create migrations for those changes.
3. Run ```python manage.py makemigrations``` to apply those changes to the database. 

## Creating an admin user

```
python manage.py createsuperuser
```
