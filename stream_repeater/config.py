""" Configuration handling """

from os import environ
import io
import sys
import yaml

class Config(object):
    """ Option-handling Object """

    def __init__(self):
        self.options = {}

    def load(self):
        """ Load config """

        print("Reading configuration file...")
        try:
            with open(environ['CONFIG']) as f:
                self.options = yaml.load(f, Loader=yaml.FullLoader)
        except:
            sys.exit("Unable to read config file, does it exist?")

        return self.options
