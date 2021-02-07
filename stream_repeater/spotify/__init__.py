""" Handle requests involving spotify """

from flask import Blueprint, current_app, render_template, abort
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import requests

spotify = Blueprint('spotify', __name__, template_folder='templates')

@spotify.route('/spotify/')
def spotify_home():
    try:
        return render_template('spotify/home.html')
    except TemplateNotFound:
        abort(404)

@spotify.route('/spotify/upload')
def spotify_upload():
    try:
        return render_template('spotify/upload.html')
    except TemplateNotFound:
        abort(404)
