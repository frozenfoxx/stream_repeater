""" Handle requests involving Beatport """

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import requests

beatport = Blueprint('beatport', __name__, template_folder='templates')

@beatport.route('/')
def beatport_home():
    try:
        return render_template('beatport/home.html')
    except TemplateNotFound:
        abort(404)

@beatport.route('/upload')
def beatport_upload():
    try:
        return render_template('beatport/upload.html')
    except TemplateNotFound:
        abort(404)