from flask import render_template
from dustinrcdotcom import app


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    name = name or "World"
    return render_template('index.html', name=name)
