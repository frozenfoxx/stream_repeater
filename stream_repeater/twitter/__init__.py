""" Handle requests involving Twitter """

from flask import Blueprint, current_app, render_template, abort
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import requests

twitter = Blueprint('twitter', __name__, template_folder='templates')

@twitter.route('/')
def twitter_home():
    try:
        return render_template('twitter/home.html')
    except TemplateNotFound:
        abort(404)
