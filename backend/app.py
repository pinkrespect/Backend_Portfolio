from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def helloWorld():
    if request.method == 'GET':
        return {"String": "HELLO, WORLD!"}
    elif request.method == 'POST':
        return 0


@app.route('/<string>', methods=['GET'])
def returnString(string):
    return {"Response": string}, 404
