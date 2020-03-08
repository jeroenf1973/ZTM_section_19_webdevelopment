# Voor het starten van server het commando:
# set FLASK_APP=server.py vanaf normale command prompt
# set FLASK_ENV=development vanaf normale command prompt
# met alleen set commando kan je checken of deze gezet is
# server vanuit (venv) opstarten met flask run

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World; Running a Flask server on my laptop!'


@app.route('/blog')
def blog():
    return 'Hier zouden blogs kunnen komen..'


@app.route('/blog/2020/dogs')
def blog2():
    return 'woef!'