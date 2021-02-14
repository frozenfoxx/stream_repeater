#!/usr/bin/env python3

if __package__:
    from .config import Config
else:
    from config import Config
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import importlib
import os
import sys

app = Flask(__name__)

import stream_repeater.views
from stream_repeater.beatport import beatport
from stream_repeater.mixcloud import mixcloud
from stream_repeater.restream import restream
from stream_repeater.spotify import spotify
from stream_repeater.telegram import telegram
from stream_repeater.twitter import twitter
from stream_repeater.youtube import youtube

app.register_blueprint(beatport)
app.register_blueprint(mixcloud)
app.register_blueprint(restream)
app.register_blueprint(spotify)
app.register_blueprint(telegram)
app.register_blueprint(twitter)
app.register_blueprint(youtube)

# This allows us to use a plain HTTP callback
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

app.config['CONFIG'] = Config().load()
app.secret_key = os.urandom(24)

if __name__ == "__main__":
    app.run()
