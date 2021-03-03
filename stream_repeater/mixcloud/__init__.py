""" Handle requests involving Mixcloud """

from flask import Blueprint, current_app, render_template, abort, Flask, request, redirect, session, url_for
from flask.json import jsonify
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import os
import requests

mixcloud = Blueprint('mixcloud', __name__, template_folder='templates')

authorization_base_url = 'https://www.mixcloud.com/oauth/authorize'
profile_url = 'https://api.mixcloud.com/me/'
token_url = 'https://www.mixcloud.com/oauth/access_token'
upload_url = 'https://api.mixcloud.com/upload/'

authorized = False

@mixcloud.route('/')
def mixcloud_home():
    try:
        return render_template('mixcloud/home.html', authorized=authorized)
    except TemplateNotFound:
        abort(404)

@mixcloud.route('/authorize')
def mixcloud_authorize():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    redirect_uri= url_for('.mixcloud_callback', _external=True)

    mixcloud_session = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = mixcloud_session.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)

@mixcloud.route('/callback', methods=["GET"])
def mixcloud_callback():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    client_secret = current_app.config['CONFIG']['accounts']['mixcloud']['client_secret']
    redirect_uri= url_for('.mixcloud_callback', _external=True)

    mixcloud_session = OAuth2Session(client_id, redirect_uri=redirect_uri, state=session['oauth_state'])
    token = mixcloud_session.fetch_token(token_url, client_secret=client_secret, include_client_id=True, code=request.args['code'])

    session['oauth_token'] = token
    
    # Now that we have a session this will let the index show we're authorized
    authorized = True

    return redirect(url_for('.mixcloud_home'))

@mixcloud.route('/profile', methods=["GET"])
def mixcloud_profile():
    """ Display the authorized user's profile """

    # Note: We would normally do this but Mixcloud requires specific parameters
    #client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    #mixcloud_session = OAuth2Session(client_id, token=session['oauth_token'])
    #return jsonify(mixcloud_session.get(profile_url))

    params = {
        "access_token": session['oauth_token']['access_token']
    }
    response = requests.get(profile_url, params)

    return redirect(response.url)

@mixcloud.route('/upload')
def mixcloud_upload():
    """ Upload a mix """

    files = {
        "mp3": "",
        "name": "",
        "picture": ""
    }
    params = {
        "access_token": session['oauth_token']['access_token']
    }
    response = requests.post(upload_url, params, files=files)

    return redirect(response.url)
