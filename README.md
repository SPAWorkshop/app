# SPA workshop application

This is application which will be developed during SPA workshop. To run both
parts of application(frontend and backend) you have to prepare Python
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
    
Create Python virtual environment:

    ~/spaworkshop $ python3 -m venv workshopenv
    
Activate newly created virtual environment:
     
    ~/spaworkshop $ source workshopenv/bin/activate

Install Python requirements:

     ~/spaworkshop (workshopenv) $ pip install -r app/backend/requirements.txt
     
Create JavaScript virtual envirnoment inside Python virtual envirnoment (you
will find more info about virtualenv installation and usage
[here](http://tutorial.djangogirls.org/django_installation/README.html)):

     ~/spaworkshop (workshopenv) $ nodeenv -p
     
Install JavaScript global development requirements:
    
    ~/spaworkshop (workshopenv) $ npm install -g bower gulp
    
Install JavaScript local development requirements:

    ~/spaworkshop/app/frontend (workshopenv) $ npm install

Installl frontend application requirements:

    ~/spaworkshop/app/frontend (workshopenv) $ bower install

That's all!