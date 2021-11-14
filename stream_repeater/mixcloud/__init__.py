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
        return render_template('mixcloud/home.html', authorized=mixcloud_status())
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
    response = requests.get(profile_url, params=params)

    return redirect(response.url)

@mixcloud.route('/status', methods=["GET"])
def mixcloud_status():
    """ Check the status of the Mixcloud session """

    if 'oauth_token' in session:
        if 'access_token' in session['oauth_token']:
            return True
        else:
            return False
    else:
        return False

@mixcloud.route('/upload')
def mixcloud_upload():
    """ Upload a mix """

    data = {
        "name": current_app.stream.title
    }

    # Build the tracklist headers and values
    for idx, val in enumerate(current_app.cuesheet.tracks):
        artistKey = "sections-" + val.track_number + "-artist"
        songKey = "sections-" + val.track_number + "-song"
        timeKey = "sections-" + val.track_number + "-start_time"
        data[artistKey] = val.performer
        data[songKey] = val.title
        data[timeKey] = val.index_time

    # Build the tags
    for idx, tag in enumerate(current_app.stream.tags):
        tagKey = "tags-" + str(idx) + "-tag"
        data[tagKey] = tag

    # Check for MP3 conversion
    if not current_app.stream.mp3_path:
        return "Stream not yet converted, please select 'Stream > convert' first"

    #FIXME: Check for banner image restrictions
    #if not current_app.stream.banner_path:
    #    return "Stream does not have a banner image, please select 'Stream' first"
    
    files = {
        "mp3": current_app.stream.mp3_path
        #FIXME "picture": current_app.stream.banner_path
    }
    params = {
        "access_token": session['oauth_token']['access_token']
    }

    response = requests.post(upload_url, data=data, params=params, files=files)

    try:
        result = response.json()
    except:
        print("Error uploading to Mixcloud")
        print(response.text)
    else:
        for key in result:
            if key == 'error':
                print('  Failure detected. Reponse text is as follows:')
                print(response.text)
            elif key == 'result':
                if result['result']['success'] == True: # These are Boolean, not strings
                    print('Upload is available at: https://mixcloud.com' + result['result']['key'])
                else:
                    print('  Failure detected. Reponse text is as follows:')
                    print(response.text)

    return redirect(response.url)
