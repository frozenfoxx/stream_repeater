#!/usr/bin/env python3
if __package__:
    from .cuesheet import CueSheet
    from .options import Options
    from .prompt import Prompt
    from .stream import Stream
else:
    from cuesheet import CueSheet
    from options import Options
    from prompt import Prompt
    from stream import Stream
import importlib
import sys

def main():
    """ Main execution thread """

    args = Options().parse_args()
    options = Options().load_options()

    # Check if running in batchmode or interactive
    if args.batchmode:
        print("Running in batchmode...")
        stream = Stream(options)
        cuesheet = CueSheet(options)

        print("Converting to MP3...")
        stream.convert_to_mp3()

        print("Loading CUE sheet...")
        cuesheet.load()
        cuesheet.dump()
    else:
        prompt = Prompt(options)
        prompt.prompt = 'stream_repeater> '
        prompt.cmdloop('Starting stream_repeater interface...')

if __name__ == "__main__":
    sys.exit(main())
