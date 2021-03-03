from flask import render_template
from stream_repeater import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404