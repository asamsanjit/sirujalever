from flask import Flask,render_template,url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/events')
def events():
	return render_template('events.html')

@app.route('/Blogs')
def blogs():
	return render_template('blogs.html')

@app.route('/videos')
def videos():
	return render_template('videos.html')

@app.route('/About-us')
def about():
	return render_template('about.html')			

if __name__ == '__main__':
	app.run(debug = True)