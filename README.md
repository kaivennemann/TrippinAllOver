# TrippinAllOver


## Description
TrippinAllOver is a web application for students in the UK who want to browse affordable weekend trips all over Europe. With this epic trip planner, you can simply input your availability for an impromptu European excursion, and you will receive recommendations for the best and cheapest placest to fly to on a budget. Head on over to [trippinallover.co.uk](https://www.trippinallover.co.uk/ "TrippinAllOver Home Page") to check it out!

Note: TrippinAllOver is currently in the development phase, so website functionality may be limited at this time.


## Django
We are using the Django web framework for this web app. The directory **src/website** serves as the root folder for our Django project, whereas the inner directory **src/website/website** is the project's Python package. The file **website/manage.py** is a useful developer command-line utility.

### Useful Commands
- `python manage.py runserver` runs the lightweight Django development server (only for development!)
    - Note: View the project in a browser at http://127.0.0.1:8000/
- `python manage.py check` screens the current project for any red flags without applying any changes or migrations
- `python manage.py shell` launches Python on the command-line with a pre-set DJANGO_SETTINGS_MODULE environment variable (thus enabling access to **settings.py**)

### Tips
- When creating models, make sure to create `__str__()` methods because they are used by *admin*


## SQLite3 Database
At the moment, we are still using the built-in sqlite3 database. Eventually, we will migrate over a larger database such as PostgreSQL.

### Useful Commands
- Run `python manage.py makemigrations [app name]` after making changes to an app's models to store those chnages as a *migration* (viewable in **[app name]/migrations**)
- `python manage.py migrate` runs migrations for the apps in INSTALLED_APPS (in **settings.py**), applying them to the database
- `python manage.py sqlmigrate [app name] 0001` prints out the SQL for a migration (without running it); this is useful if you want to double-check before actually migrating to the database
- `sqlite3 db.sqlite3` in **src/website** to access the database on the command-line with standard SQL
    - `.tables` then shows all the tables currently stored


## Apache Web Server
We are running an Apache web server on Ubuntu. The server is WSGI-compatible, meaning that it looks for the file **src/website/website/wsgi.py** as an entry-point to serve our Django project.

### Useful Commands
- `ssh [user@servername] -p [port number]` to access the server
- `exit` to exit the server
- `sudo nano /etc/apache2/sites-available/000-default.conf` to edit the server configurations
- `sudo systemctl restart apache2` to restart the server (e.g. after modifying the config)


## Deployment
Before deploying, there are a few things to take care of:
- Run `python manage.py collectstatic` to create copies of static files, which the server can then service more quickly (this speeds up the web page UI)
- Make sure to create and and run any new migrations (refer to **Useful Commands** under **SQLite3 Database**)


## Build History

### Django Project Setup
- `django-admin startproject website` auto-generates the project files
- Run `python manage.py startapp [app name]` in **src/website** to create a new app (such as *booking* or *flightsapi* etc.), which then provides a specific functionality to our overall project
- `python manage.py createsuperuser` to create admin accounts

### Apache Web Server Setup

Apache Configuration:
```xml
<VirtualHost *:443>
    ServerName trippinallover.co.uk
    ServerAlias www.trippinallover.co.uk
    WSGIScriptAlias / /home/kaiv/webapp/TrippinAllOver/wsgi.py
    WSGIDaemonProcess TrippinAllOver python-path=/home/kaiv/webapp/TrippinAllOver python-home=/home/kaiv/webapp/TrippinAllOver/.venv
    WSGIProcessGroup TrippinAllOver
        <IfModule mod_headers.c>
               Header set Access-Control-Allow-Origin "*"
        </IfModule>

    DocumentRoot /home/kaiv/webapp/TrippinAllOver
    <Directory /home/kaiv/webapp/TrippinAllOver >
        Options -Indexes +FollowSymLinks -MultiViews
        AllowOverride None
        Require all granted
    </Directory>

    Alias /static/ /home/kaiv/webapp/TrippinAllOver/collected_static/
    <Directory /home/kaiv/webapp/TrippinAllOver/collected_static>
        Require all granted
    </Directory>

    <Directory /home/kaiv/webapp/TrippinAllOver/src/website/website>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
</VirtualHost>
```
The Apache configuration above links together (literally) our web domain with the Django project code on our server. Step by step, the config does the following:
- Defines a new virtual host that monitors incoming traffic on port 443 (which is the HTTPS standard port)
- Sets this virtual host's base domain name ([trippinallover.co.uk](www.trippinallover.co.uk)) and an alias for the server name
- `WSGIScriptAlias` tells Apache to redirect any requests going to the root URL (`/`) to our WSGI app (`wsgi.py`)
- Configures a `mod_wsgi` daemon process (`WSGIDaemonProcess`) named "TrippinAllOver" to run our Python web app with the specified Python path (i.e. the path to our Python project) and virtual environment
    - Note: The daemon process is a background process that handles incoming requests to our WSGI application
- Sets the daemon process group to be the daemon process we configured above
- Sets some options for specific directories
    - Note: `Require all granted` allows access to a directory from all hosts
- Sets the document root (i.e. the directory within the server) for the project
- Specifies the filesystem path from which static files will be served


## TO DO
    - Testing
        - Write unit tests for each app (see https://docs.djangoproject.com/en/4.2/topics/testing/)
        - Write in-browser tests using Selenium and Django's LiveServerTestCase
    - Install and set up Django Debug Toolbar