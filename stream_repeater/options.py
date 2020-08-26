""" Configuration loading and argument handling """

import argparse
import io
import sys
import os
import yaml

class Options(object):
    """ Option-handling Object """

    def __init__(self):
        self.options = {}

    def parse_args(self):
        """ Parse optional arguments """

        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--config", dest="config", default="/etc/stream_repeater/conf/stream_repeater.yaml", type=str, help="path to config file")
        args = parser.parse_args()

        return args

    def load_options(self):
        """ Load options and overrides """

        args = self.parse_args()

        print("[+] Reading configuration file")
        try:
            with open(args.config) as f:
                print("[+] Loading options from file")
                self.options = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            sys.exit("Unable to read config file, does it exist?")

        return self.options
