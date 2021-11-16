#!/usr/bin/env python3

from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
from os import environ
import importlib
import sys

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("stream_repeater.config.ProdConfig")
else:
    app.config.from_object("stream_repeater.config.DevConfig")

import stream_repeater.views
from stream_repeater.beatport import beatport
from stream_repeater.mixcloud import mixcloud
from stream_repeater.restream import restream
from stream_repeater.spotify import spotify
from stream_repeater.stream import stream
from stream_repeater.telegram import telegram
from stream_repeater.youtube import youtube

app.register_blueprint(beatport, url_prefix='/beatport')
app.register_blueprint(mixcloud, url_prefix='/mixcloud')
app.register_blueprint(restream, url_prefix='/restream')
app.register_blueprint(spotify, url_prefix='/spotify')
app.register_blueprint(stream, url_prefix='/stream')
app.register_blueprint(telegram, url_prefix='/telegram')
app.register_blueprint(youtube, url_prefix='/youtube')

if __name__ == "__main__":
    app.run()
