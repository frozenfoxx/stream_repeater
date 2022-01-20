#!/usr/bin/env python3

from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("stream_repeater.config.ProdConfig")
else:
    app.config.from_object("stream_repeater.config.DevConfig")

import stream_repeater.views
from stream_repeater.mixcloud import mixcloud
from stream_repeater.stream import stream

app.register_blueprint(mixcloud, url_prefix='/mixcloud')
app.register_blueprint(stream, url_prefix='/stream')

if __name__ == "__main__":
    app.run()
