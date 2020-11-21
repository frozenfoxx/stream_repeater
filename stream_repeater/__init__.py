#!/usr/bin/env python3
if __package__:
    from .cuesheet import CueSheet
    from .options import Options
    from .prompt import Prompt
    from .stream import Stream
else:
    from cuesheet import CueSheet
    from options import Options
    from prompt import Prompt
    from stream import Stream

from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import importlib
import os
import sys

def main():
    """ Main execution thread """

    args = Options().parse_args()
    options = Options().load_options()

    # Check if running in server interactive
    if args.interactive:
        prompt = Prompt(options)
        prompt.prompt = 'stream_repeater> '
        prompt.cmdloop('Starting stream_repeater interface...')
        sys.exit()

    # Not interactive, start server
    stream = Stream(options)
    cuesheet = CueSheet(options)

    print("Loading CUE sheet...")
    cuesheet.load()
    cuesheet.dump()

    print("Converting to MP3...")
    stream.convert_to_mp3()

    print("Running server...")
    app = Flask(__name__)
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    sys.exit(main())
