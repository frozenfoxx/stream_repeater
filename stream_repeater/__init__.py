#!/usr/bin/env python3
if __package__:
    from .cuesheet import CueSheet
    from .options import Options
    from .stream import Stream
else:
    from cuesheet import CueSheet
    from options import Options
    from stream import Stream
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import importlib
import os
import sys

options = Options().load_options()

stream = Stream(options)
cuesheet = CueSheet(options)

print("Loading CUE sheet...")
cuesheet.load()
cuesheet.dump()

print("Converting to MP3...")
stream.convert_to_mp3()

print("Running server...")
app = Flask(__name__)

import stream_repeater.views

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
