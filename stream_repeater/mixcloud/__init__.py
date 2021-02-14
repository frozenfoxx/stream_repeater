""" Handle requests involving Mixcloud """

from flask import Blueprint, current_app, render_template, abort, Flask, request, redirect, session, url_for
from flask.json import jsonify
from jinja2 import TemplateNotFound
from requests_oauthlib import OAuth2Session
import os

mixcloud = Blueprint('mixcloud', __name__, template_folder='templates')

authorization_base_url = 'https://www.mixcloud.com/oauth/authorize'
token_url = 'https://www.mixcloud.com/oauth/access_token'

client_id = ""
client_secret = ""
redirect_uri = ""

@mixcloud.route('/mixcloud/')
def mixcloud_home():
    try:
        mixcloud_setup()
        return render_template('mixcloud/home.html')
    except TemplateNotFound:
        abort(404)

@mixcloud.route('/mixcloud/authorize')
def mixcloud_authorize():
    mixcloud_session = OAuth2Session(client_id)
    authorization_url, state = mixcloud_session.authorization_url(authorization_base_url)

    session['oauth_state'] = state
    return redirect(authorization_url)

@mixcloud.route('/mixcloud/callback', methods=["GET"])
def mixcloud_callback():
    mixcloud_session = OAuth2Session(client_id, state=session['oauth_state'])
    token = mixcloud_session.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)

    session['oauth_token'] = token

    return redirect(url_for('.profile'))

@mixcloud.route("/mixcloud/profile", methods=["GET"])
def mixcloud_profile():
    github = OAuth2Session(client_id, token=session['oauth_token'])
    return jsonify(github.get('https://api.mixcloud.com/user').json())

@mixcloud.route('/mixcloud/upload')
def mixcloud_upload():
    try:
        return render_template('mixcloud/upload.html')
    except TemplateNotFound:
        abort(404)

def mixcloud_setup():
    client_id = current_app.config['CONFIG']['accounts']['mixcloud']['client_id']
    client_secret = current_app.config['CONFIG']['accounts']['mixcloud']['client_secret']
    redirect_uri = "http://" + current_app.config['CONFIG']['system']['fqdn'] + "/mixcloud/callback"
