""" Handle requests involving Mixcloud """

from flask import Blueprint, current_app, render_template, abort, Flask, request, redirect, session, url_for
from flask.json import jsonify
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import os

mixcloud = Blueprint('mixcloud', __name__, template_folder='templates')

authorization_base_url = 'https://www.mixcloud.com/oauth/authorize'
profile_url = 'https://api.mixcloud.com/me/'
token_url = 'https://www.mixcloud.com/oauth/access_token'

@mixcloud.route('/')
def mixcloud_home():
    try:
        return render_template('mixcloud/home.html')
    except TemplateNotFound:
        abort(404)

@mixcloud.route('/authorize')
def mixcloud_authorize():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    redirect_uri = "http://" + current_app.config['CONFIG']['system']['fqdn'] + "/mixcloud/callback"

    mixcloud_session = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = mixcloud_session.authorization_url(authorization_base_url)

    session['oauth_state'] = state

    return redirect(authorization_url)

@mixcloud.route('/callback', methods=["GET"])
def mixcloud_callback():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    client_secret = current_app.config['CONFIG']['accounts']['mixcloud']['client_secret']

    mixcloud_session = OAuth2Session(client_id, state=session['oauth_state'])
    token = mixcloud_session.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)

    session['oauth_token'] = token

    return redirect(url_for('.profile'))

@mixcloud.route('/profile', methods=["GET"])
def mixcloud_profile():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']

    mixcloud_session = OAuth2Session(client_id, token=session['oauth_token'])
    return jsonify(mixcloud_session.get(profile_url).json())

@mixcloud.route('/upload')
def mixcloud_upload():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    client_secret = current_app.config['CONFIG']['accounts']['mixcloud']['client_secret']
    redirect_uri = "http://" + current_app.config['CONFIG']['system']['fqdn'] + "/mixcloud/callback"

    try:
        return render_template('mixcloud/upload.html')
    except TemplateNotFound:
        abort(404)
