from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!<p><br><a href="/about">About</a>'

@app.route('/about')
def talk_about():
	return '<p>This app runs using the Flask web framework<p><br><a href="https://flask.palletsprojects.com/en/stable/">Check out the framework here</a>'
