""" Configuration handling """

if __package__:
    from .options import Options
else:
    from options import Options
from os import environ

class Config:
    """ Base config """

    # This allows us to use a plain HTTP callback
    environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    SECRET_KEY = environ.get('SECRET_KEY')

class DevConfig(Config):
    FLASK_ENV = 'development'
    options = Options()
    CONFIG = options.load()
    DEBUG = True
    TESTING = True

class ProdConfig(Config):
    FLASK_ENV = 'production'
    options = Options()
    CONFIG = options.load()
    DEBUG = False
    TESTING = False
