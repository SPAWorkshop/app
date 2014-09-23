# SPA workshop application

This is application which will be developed during SPA workshop. To run both
parts of application (frontend and backend) you have to prepare Python
[virtualenv](http://virtualenv.readthedocs.org) with all requirements. First
of all we need to install Python 3.4 and Git.

## Install Python

Linux (Ubuntu):

    $ apt-get install python3

Mac OS X (with brew):

    $ brew install python3

For more details you should check this
[tutorial](http://tutorial.djangogirls.org/python_installation/README.html).

## Install Git

Linux (Ubuntu):

    $ apt-get install git

Mac OS X (with brew):

    $ brew install git

## Install application requirements

Create directory for all workshop files:

    $ mkdir spaworkshop

Clone SPA workshop repository (inside `spaworkshop` directory):

    ~/spaworkshop $ git clone git@github.com:SPAWorkshop/app.git
    
Create Python virtual environment (you
will find more info about virtualenv installation and usage
[here](http://tutorial.djangogirls.org/django_installation/README.html)):

    ~/spaworkshop $ python3 -m venv workshopenv
    
Activate newly created virtual environment:
     
    ~/spaworkshop $ source workshopenv/bin/activate

Install Python requirements:

     ~/spaworkshop (workshopenv) $ pip install -r app/backend/requirements.txt
     
Create JavaScript virtual envirnoment inside Python virtual environment:

     ~/spaworkshop (workshopenv) $ ./workshopenv/bin/nodeenv -p
     
Install JavaScript global development requirements:
    
    ~/spaworkshop (workshopenv) $ ./workshopenv/bin/npm install -g bower gulp
    
Install JavaScript local development requirements (don't worry about `node-gyp`
installation errors - it's optional dependency):

    ~/spaworkshop/app/frontend (workshopenv) $ ../../workshopenv/bin/npm install

Installl frontend application requirements:

    ~/spaworkshop/app/frontend (workshopenv) $ ../../workshopenv/bin/bower install

That's all!

## Run backend application

Create local database:

    ~/spaworkshop/app/backend (workshopenv) $ ./manage.py migrate


Fill database wih testing data:

    ~/spaworkshop/app/backend (workshopenv) $ ./manage.py filldb


Run development server:

    ~/spaworkshop/app/backend (workshopenv) $ ./manage.py runserver


## Run frontend application

Run development server (in another terminal, remember to activate virtualenv):

    ~/spaworkshop/app/fronted (workshopenv) $ ../../workshopenv/bin/gulp serve
