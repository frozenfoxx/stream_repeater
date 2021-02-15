""" Handle requests involving Telegram """

from flask import Blueprint, current_app, render_template, abort
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import requests

telegram = Blueprint('telegram', __name__, template_folder='templates')

@telegram.route('/')
def telegram_home():
    try:
        return render_template('telegram/home.html')
    except TemplateNotFound:
        abort(404)
