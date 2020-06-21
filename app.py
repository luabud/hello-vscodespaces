from flask import Flask

app = flask.run()

@app.route('/')
def index():
    return "Hello, VS Codespaces!"
