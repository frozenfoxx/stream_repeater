if __package__:
    from .config import Config
    from .cuesheet import CueSheet
    from .stream import Stream
else:
    from config import Config
    from cuesheet import CueSheet
    from stream import Stream
from flask import render_template
from stream_repeater import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/convert')
def convert():
    return render_template('convert.html')

@app.route('/convert/mp3')
def convert_to_mp3():
    config = Config().load()
    stream = Stream(config)
    stream.convert_to_mp3()
    return "Stream converted"

@app.route('/cuesheet')
def cuesheet():
    config = Config().load()
    cuesheet = CueSheet(config)
    cuesheet.load()

    header = cuesheet.header
    tracks = cuesheet.tracks
    return render_template('cuesheet.html', header=header, tracks=enumerate(tracks))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404