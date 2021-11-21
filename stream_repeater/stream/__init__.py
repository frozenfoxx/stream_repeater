""" Handle requests involving streams """

if __package__:
    from .cuesheet import CueSheet
    from .historysheet import HistorySheet
    from .stream import Stream
else:
    from cuesheet import CueSheet
    from historysheet import HistorySheet
    from stream import Stream
from flask import Blueprint, current_app, render_template, abort, Flask, request, redirect, session, url_for
from flask.json import jsonify
from jinja2 import TemplateNotFound

stream = Blueprint('stream', __name__, template_folder='templates')

@stream.before_app_first_request
def stream_init():
    current_app.stream = Stream(current_app.config['CONFIG'])

    # Load a CUE sheet if found, fall back to History sheet
    if 'cuesheet' in current_app.config['CONFIG']['stream']:
        current_app.cuesheet = CueSheet(current_app.config['CONFIG'])
        current_app.cuesheet.load()
    elif 'historysheet' in current_app.config['CONFIG']['stream']:
        current_app.historysheet = HistorySheet(current_app.config['CONFIG'])
        current_app.historysheet.load()

@stream.route('/')
def stream_home():
    try:
        return render_template('stream/home.html')
    except TemplateNotFound:
        abort(404)

@stream.route('/convert/mp3')
def stream_convert_to_mp3():
    current_app.stream.convert_to_mp3()
    try:
        return render_template('stream/convert.html', success=True)
    except TemplateNotFound:
        abort(404)

@stream.route('/cuesheet')
def stream_cuesheet():
    header = current_app.cuesheet.header
    tracks = current_app.cuesheet.tracks

    if not current_app.cuesheet:
        return "cuesheet not defined"

    try:
        return render_template('stream/cuesheet.html', header=header, tracks=enumerate(tracks))
    except TemplateNotFound:
        abort(404)

@stream.route('/historysheet')
def stream_historysheet():
    tracks = current_app.historysheet.tracks

    if not current_app.historysheet:
        return "historysheet not defined"

    try:
        return render_template('stream/historysheet.html', tracks=enumerate(tracks))
    except TemplateNotFound:
        abort(404)

@stream.route('/status')
def stream_status():
    try:
        return render_template('stream/status.html',
            title=current_app.stream.title,
            album=current_app.stream.album,
            bitrate=current_app.stream.bitrate,
            cover_path=current_app.stream.cover_path,
            mp3file=current_app.stream.mp3file,
            performer=current_app.stream.performer,
            sourcefile=current_app.stream.sourcefile,
            tags=enumerate(current_app.stream.tags))
    except TemplateNotFound:
        abort(404)