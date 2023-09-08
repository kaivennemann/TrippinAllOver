# TrippinAllOver

## Description
TrippinAllOver is a web application for students in the UK who want to browse affordable weekend trips all over Europe. With this epic trip planner, you can simply input your availability for an impromptu European excursion, and you will receive recommendations for the best and cheapest placest to fly to on a budget. Head on over to [trippinallover.co.uk] to check it out!

Note: TrippinAllOver is currently in the development phase, so website functionality may be limited at this time.

## Django
We are using the Django web framework for this web app. The directory **src/website** serves as the root folder for our Django project, whereas the inner directory **src/website/website** is the project's Python package. The file **website/manage.py** is a useful developer command-line utility.

### Useful Commands
- `python -m django --version`
- `python manage.py runserver` runs the lightweight Django development server (only for development!)
    - Note: View the project in a browser at [http://127.0.0.1:8000/]
- Run `python manage.py startapp [app name]` in **src/website** to create a new app (such as *booking* or *flightsapi* etc.)



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

## Build History

### Django Project Setup
- `django-admin startproject website` auto-generates the project files



### Apache Web Server Setup
- TODO