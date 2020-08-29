""" Interactive Prompt """

if __package__:
    from .options import Options
else:
    from options import Options
import os
import sys
import yaml
from cmd import Cmd
from pydub import AudioSegment

class Prompt(Cmd, object):
    """ Handle user input """

    def __init__(self, options):
        super(Prompt, self).__init__()

        self.options = options

    def do_options(self, args):
        """ List loaded options """

        print(yaml.dump(self.options))

    def do_convert_to_mp3(self, args):
        """ Convert a recording to MP3
            convert_to_mp3 """

        # Check argument list
        if len(args) == 0:
            print("Error: argument list cannot be empty")
        elif len(args.split()) != 1:
            print("Error: argument list incorrect")
        else:
            filename = self.options.stream.filename
            recording = AudioSegment.from_wav(filename)
            recording_base_name = os.path.splitext(filename)[0]
            mp3_filename = recording_base_name + ".mp3"
            recording.export(
                mp3_filename,
                bitrate="320k",
                format="mp3",
                tags={
                    'artist': 'Various artists',
                    'album': 'Streams'
                    }
                )
            
            printf("Converted " + filename + " to " + mp3_filename)

    def do_quit(self, args):
        """ Quit the program """

        print("Shutting down...")

        raise SystemExit
