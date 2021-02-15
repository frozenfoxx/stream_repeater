""" Handle requests involving YouTube """

from flask import Blueprint, current_app, render_template, abort
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import requests

youtube = Blueprint('youtube', __name__, template_folder='templates')

@youtube.route('/')
def youtube_home():
    try:
        return render_template('youtube/home.html')
    except TemplateNotFound:
        abort(404)

@youtube.route('/upload')
def youtube_upload():
    try:
        return render_template('youtube/upload.html')
    except TemplateNotFound:
        abort(404)
