""" Handle requests involving Mixcloud """

from flask import Blueprint, render_template, abort
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

@mixcloud.route('/mixcloud/upload')
def mixcloud_upload():
    try:
        return render_template('mixcloud/upload.html')
    except TemplateNotFound:
        abort(404)

class Mixcloud(object):
    """ Mixcloud-handling Object """

    def __init__(self):
        self.token = ''
        self.upload_url = 'https://api.mixcloud.com/upload/'

    def authorize(self, oauth):
        """ Create an authorized session with Mixcloud """

    def upload(self, cuesheet, stream):
        """ Upload a mix to Mixcloud """

        cuesheet = cuesheet
        stream = stream

        # Build the upload URL
        url = self.upload_url + "?access_token=" + self.token

        payload = {
            'mp3': stream.filename,
            'name': stream.title
        }
        requests.post(url, data=payload)
