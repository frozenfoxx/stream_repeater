""" Configuration loading and argument handling """

import argparse
import io
import os
import sys
import yaml

class Options(object):
    """ Option-handling Object """

    def __init__(self):
        self.config_path = "/etc/stream_repeater/conf/stream_repeater.yaml"
        self.options = {}

    def load_options(self):
        """ Load options and overrides """

        print("Reading configuration file...")
        try:
            with open(self.config_path) as f:
                self.options = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            sys.exit("Unable to read config file, does it exist?")

        return self.options
