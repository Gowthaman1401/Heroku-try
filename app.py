from flask import Flask, jsonify
import gunicorn

app = Flask(__name__)

@app.route('/')
@app.route('/hello_world')

def hello_world():
	return "Hello World"

@app.route('/ans')

def ans():
    file = open("file.txt", "r")
    text = file.read()
    file.close()
    return jsonify(text)


if __name__ == '__main__':
	app.run()