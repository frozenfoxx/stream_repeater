""" Option handling """

from os import environ
import sys
import yaml

class Options:
    """ Configuration options specific to stream_repeater """

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
