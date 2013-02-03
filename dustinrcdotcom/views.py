from dustinrcdotcom import app


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    name = name or "World"
    return "Hello {}! Good to see you...".format(name)
