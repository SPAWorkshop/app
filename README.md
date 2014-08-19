# SPA workshop application

Instalation:

    $ mkvirtualenv -p python3.4 spaworkshop
    $ cd backend/
    $ pip install -r requirements.txt
    $ ./manage.py migrate
    $ cd ../frontend
    $ nodeenv -p
    $ npm install -g yo bower gulp generator-gulp-angular
    $ npm install
    $ bower install

Run frontend app:

    $ cd frontend/
    $ gulp serve

Run backend app:

    $ cd backend/
    $ ./manage.py runserver
