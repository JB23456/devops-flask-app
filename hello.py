from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Welcome!<p><br><a href="/about">About</a><br><a href="/contact">Contact</a>'

@app.route('/about')
def talk_about():
	return '<p>This app runs using the Flask web framework<p><br><a href="https://flask.palletsprojects.com/en/stable/">Check out the framework here</a>'


@app.route('/contact')
def contact_info():
	return '<p>Email: C24733535@mytudublin.ie<p>'
