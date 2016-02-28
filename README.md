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

1. Install python-mysql

For Python 3:

```
pip install PyMySQL
```


