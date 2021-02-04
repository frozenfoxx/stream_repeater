#!/usr/bin/env python3

from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import importlib
import os
import sys

app = Flask(__name__)

import stream_repeater.views
from stream_repeater.mixcloud import mixcloud

app.register_blueprint(mixcloud)

if __name__ == "__main__":
    app.run()
