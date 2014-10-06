# SPA workshop application

This is application which will be developed during SPA workshop. To run both
parts of application (frontend and backend) you have to prepare Python
[virtualenv](http://virtualenv.readthedocs.org) with all requirements. First
of all we need to install Python **3.4** and Git.

## Install Python

Linux (Ubuntu):

    $ apt-get install python3

Mac OS X (with brew):

    $ brew install python3

Check Python version - it should be 3.4:

    $ python3 --version
    Python 3.4.1

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

    ~/spaworkshop $ git clone https://github.com/SPAWorkshop/app.git
    
Create Python virtual environment (you
will find more info about virtualenv installation and usage
[here](http://tutorial.djangogirls.org/django_installation/README.html)):

    ~/spaworkshop $ python3 -m venv workshopenv
    
Activate newly created virtual environment:
     
    ~/spaworkshop $ source workshopenv/bin/activate

Install Python requirements:

     ~/spaworkshop (workshopenv) $ pip install -r app/backend/requirements.txt
     
Create JavaScript virtual environment inside Python virtual environment (this
can take a few minutes):

     ~/spaworkshop (workshopenv) $ ./workshopenv/bin/nodeenv -p
     
Install JavaScript global development requirements:
    
    ~/spaworkshop (workshopenv) $ ./workshopenv/bin/npm install -g bower gulp
    
Install JavaScript local development requirements (don't worry about `node-gyp`
installation errors - it's optional dependency):

    ~/spaworkshop/app/frontend (workshopenv) $ ../../workshopenv/bin/npm install

Install frontend application requirements:

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

## Troubleshooting 

### There is no `pip` inside your virtualenv

You are trying to install Python requirements and you have problem with
permissions, e.g.:

    OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/...'

There could be many reasons:

1. You are outside virtualenv (check above how to activate virtualenv).
2. Virtualenv was created with wrong version of Python. You have to use
Python 3.4. Check current Python version inside virtualenv with following
command: `python --version`.
3. You are using Ubuntu - check this
[bug](https://bugs.launchpad.net/ubuntu/+source/python3.4/+bug/1290847).
In this case you should install [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation)
separately and create virtualenv with command `virtualenv -p python3 workshopenv`.

### You couldn't install `node.js` inside virtualenv

You are trying to install `node.js` with `nodenv -p` command and you have
following error:

    OSError: Python >=3.0 virtualenv detected, but no python2 command (required for building node.js) was found

Unfortunately, `nodenv` required `python2` command within your `PATH`. If you
don't have `python2`, but there is `python2.7`, please create this link:

    $ sudo ln -s `which python2.7` $(dirname `which python2.7`)/python2
    
### You have problem with `node.js` requirements

You are trying to install `node.js` requirements (`npm install`) and you have
following errors:

    npm ERR! EEXIST, open '~/.npm/5cde87d1-npm-gulp-util-2-2-20-package-tgz.lock'
    File exists: ~/.npm/5cde87d1-npm-gulp-util-2-2-20-package-tgz.lock
    Move it away, and try again. 

You could try to remove `node_modules` folder, clean cache, and install
everything again:

    ~/spaworkshop/app/frontend (workshopenv) $ rm -r node_modules
    ~/spaworkshop/app/frontend (workshopenv) $ ../../workshopenv/bin/npm cache clean
    ~/spaworkshop/app/frontend (workshopenv) $ ../../workshopenv/bin/npm install
    
If this doesn't solve the problem, try downgrade `npm` to `1.3` version:

    ~/spaworkshop/app/frontend (workshopenv) $ ../../workshopenv/bin/npm -g install npm@1.3

... or upgrade to `2.1`:

    ~/spaworkshop/app/frontend (workshopenv) $ ../../workshopenv/bin/npm -g install npm@2.1
    
After `npm` downgrade/upgrade repeat all above steps (remove `node_modules`
folder, clean cache, install requirements).
