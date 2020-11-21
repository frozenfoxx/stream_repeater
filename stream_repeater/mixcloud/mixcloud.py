""" Handle requests involving Mixcloud """
from flask import Flask, jsonify
from authlib.integrations.flask_client import OAuth
import requests

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
