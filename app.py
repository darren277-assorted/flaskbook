from flask import Flask

from settings import PORT

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world.'

app.run(port=PORT)


