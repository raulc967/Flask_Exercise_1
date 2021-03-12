# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = request.args.get("a")
    b = request.args.get("b")
    answer = int(a) + int(b)
    return f"{answer}"

@app.route('/sub')
def subtraction():
    a = request.args.get("a")
    b = request.args.get("b")
    answer = int(a) - int(b)
    return f"{answer}"

@app.route('/mult')
def multiplication():
    a = request.args.get("a")
    b = request.args.get("b")
    answer = int(a) * int(b)
    return f"{answer}"

@app.route('/div')
def division():
    a = request.args.get("a")
    b = request.args.get("b")
    answer = int(a) / int(b)
    return f"{answer}"

@app.route('/math/<operation>')
def math(operation):
    oper = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }
    a = request.args.get("a")
    b = request.args.get("b")
    answer = oper[operation](int(a), int(b))
    return str(answer)