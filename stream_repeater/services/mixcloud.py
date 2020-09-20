""" Handle requests involving Mixcloud """
import requests

class Mixcloud(object):
    """ Mixcloud-handling Object """

    def __init__(self, token, stream, cuesheet):
        self.base_url = 'https://api.mixcloud.com'
        self.cuesheet = cuesheet
        self.stream = stream
        self.token = token

    def upload(self):
        """ Upload a mix to Mixcloud """

        # Build the upload URL
        url = self.base_url + "/upload/?access_token=" + self.token

        payload = {
            'mp3': self.stream.filename,
            'name': self.stream.title
        }
        requests.post(url, data=payload)
