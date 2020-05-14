from flask import Flask

app = Flask.run()

@app.route('/')
def index():
    return "Hello, VS Codespaces!"
