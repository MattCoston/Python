from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="Matt"):
	return "Hello {}".format(name)





app.run(debug=True, port=80, host='127.0.0.1')