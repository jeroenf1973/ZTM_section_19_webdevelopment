# Voor het starten van server het commando:
# set FLASK_APP=server.py vanaf normale command prompt
# set FLASK_ENV=development vanaf normale command prompt
# met alleen set commando kan je checken of deze gezet is
# server vanuit (venv) opstarten met flask run

from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello World; Running a Flask server on my laptop!'
    # render template gebruit standaard template folder
    print(url_for('static', filename='favicon.ico'))
    return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon:
#     return ''

@app.route('/users/<username>/<int:post_id>')
def username(username=None, post_id=None):
    return render_template('about.html', name=username, post_id=post_id)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return 'Hier zouden blogs kunnen komen..'


@app.route('/blog/2020/dogs')
def blog2():
    return 'woef!'