""" Handle requests involving Twitter """

from flask import Blueprint, current_app, render_template, abort, Flask, request, redirect, session, url_for
from flask.json import jsonify
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import os

twitter = Blueprint('twitter', __name__, template_folder='templates')

authorization_base_url = 'https://www.twitter.com/oauth/authorize'
profile_url = 'https://api.twitter.com/me/'
token_url = 'https://www.twitter.com/oauth/access_token'

@twitter.route('/')
def twitter_home():
    try:
        return render_template('twitter/home.html')
    except TemplateNotFound:
        abort(404)

@twitter.route('/authorize')
def twitter_authorize():
    client_id = current_app.config['CONFIG']['accounts']['twitter']['client_id']
    redirect_uri = "http://" + current_app.config['CONFIG']['system']['fqdn'] + "/twitter/callback"

    twitter_session = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = twitter_session.authorization_url(authorization_base_url)
    
    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state

    return redirect(authorization_url)

@twitter.route('/callback', methods=["GET"])
def twitter_callback():
    client_id = current_app.config['CONFIG']['accounts']['twitter']['client_id']
    client_secret = current_app.config['CONFIG']['accounts']['twitter']['client_secret']

    twitter_session = OAuth2Session(client_id, state=session['oauth_state'])
    token = twitter_session.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)

    session['oauth_token'] = token

    return redirect(url_for('.profile'))

@twitter.route('/profile', methods=["GET"])
def twitter_profile():
    client_id = current_app.config['CONFIG']['accounts']['twitter']['client_id']

    twitter_session = OAuth2Session(client_id, token=session['oauth_token'])
    return jsonify(twitter_session.get(profile_url).json())

@twitter.route('/upload')
def twitter_upload():
    client_id = current_app.config['CONFIG']['accounts']['twitter']['client_id']
    client_secret = current_app.config['CONFIG']['accounts']['twitter']['client_secret']
    redirect_uri = "http://" + current_app.config['CONFIG']['system']['fqdn'] + "/twitter/callback"

    try:
        return render_template('twitter/upload.html')
    except TemplateNotFound:
        abort(404)
