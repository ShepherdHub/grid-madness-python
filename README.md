# Introduction

This repository is the python back end for a grid-based path-finding application. The front end portion sends a payload describing the grid size, important points on the grid, and the alogorithm to use to find the shortest path. [Flask](http://flask.pocoo.org/) is used to handle the request and serve up the coordinates of the calculated shortest path.

# Running the application locally

1. Install Python 2.7 (or use your favorite python environment manager to create a python 2.7 environment)
1. If using a virutal environment, activate it now
1. Install Flask by running `pip install Flask`
1. Set the Flask application environment variable
   - Linux/OSX
   ```
   $ export FLASK_APP=webservice.py
   ```
   - Windows Command Line
   ```
   C:\path\to\app>set FLASK_APP=webservice.py
   ```
   - Windows Power Shell
   ```
   PS C:\path\to\app> $env:FLASK_APP = "webservice.py"
   ```
1. Run the application
   ```
   $ flask run
       * Running on http://127.0.0.1:5000/
   ```
