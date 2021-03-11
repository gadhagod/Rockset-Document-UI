import flask
from json import loads

app = flask.Flask(__name__, template_folder='.')
api_key = loads(open('config.json', 'r').read())['api_key']

@app.route('/')
def home():
    return flask.redirect(flask.url_for('add'))

@app.route('/add')
def add():
    return(flask.render_template('add.html', api_key=api_key))

@app.route('/delete')
def delete():
    return(flask.render_template('delete.html', api_key=api_key))

app.run(debug=True)