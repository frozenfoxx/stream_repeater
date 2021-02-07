""" Handle requests involving Mixcloud """

from flask import Blueprint, current_app, render_template, abort
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import requests

mixcloud = Blueprint('mixcloud', __name__, template_folder='templates')

@mixcloud.route('/mixcloud/')
def mixcloud_home():
    try:
        return render_template('mixcloud/home.html')
    except TemplateNotFound:
        abort(404)

@mixcloud.route('/mixcloud/authorize')
def mixcloud_authorize():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    client_secret = current_app.config['CONFIG']['accounts']['mixcloud']['client_secret']
    redirect_uri = ''

    return

@mixcloud.route('/mixcloud/upload')
def mixcloud_upload():
    try:
        return render_template('mixcloud/upload.html')
    except TemplateNotFound:
        abort(404)
