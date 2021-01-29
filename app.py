from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    pass


def multi(num):
    return num * 3


def diff(num):
    return num - 2


def add(num):
    return num + 2


if __name__ == '__main__':
    app.run(debug=True)
