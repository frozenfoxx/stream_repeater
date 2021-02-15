""" Handle requests involving Restream """

from flask import Blueprint, current_app, render_template, abort
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import requests

restream = Blueprint('restream', __name__, template_folder='templates')

@restream.route('/')
def restream_home():
    try:
        return render_template('restream/home.html')
    except TemplateNotFound:
        abort(404)

@restream.route('/upload')
def restream_upload():
    try:
        return render_template('restream/upload.html')
    except TemplateNotFound:
        abort(404)
