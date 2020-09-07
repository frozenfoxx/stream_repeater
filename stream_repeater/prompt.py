""" Interactive Prompt """

if __package__:
    from .cuesheet import CueSheet
    from .options import Options
    from .stream import Stream
else:
    from cuesheet import CueSheet
    from options import Options
    from stream import Stream
import os
import sys
import yaml
from cmd import Cmd

class Prompt(Cmd, object):
    """ Handle user input """

    def __init__(self, options):
        super(Prompt, self).__init__()

        self.options = options
        self.cuesheet = CueSheet(self.options)
        self.stream = Stream(self.options)

    def do_options(self, args):
        """ List loaded options """

        print(yaml.dump(self.options))

    def do_convert_to_mp3(self, args):
        """ Convert a recording to MP3
            convert_to_mp3 """

        # Check argument list
        if len(args) > 0:
            print("Error: method does not take arguments")
        else:
            self.stream.convert_to_mp3()

    def do_read_cuesheet(self, args):
        """ Read the CUE sheet
            read_cuesheet """

        # Check argument list
        if len(args) > 0:
            print("Error: method does not take arguments")
        else:
            self.cuesheet.read()

    def do_quit(self, args):
        """ Quit the program """

        print("Shutting down...")

        raise SystemExit
