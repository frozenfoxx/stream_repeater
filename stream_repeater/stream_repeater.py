#!/usr/bin/env python3
if __package__:
    from .options import Options
    from .prompt import Prompt
else:
    from options import Options
    from prompt import Prompt
import importlib
import sys

def main():
    """ Main execution thread """

    args = Options().parse_args()
    options = Options().load_options()

    # Check if running in batchmode or interactive
    if args.batchmode:
        print("Running in batchmode...")
    else:
        prompt = Prompt(options)
        prompt.prompt = 'stream_repeater> '
        prompt.cmdloop('Starting stream_repeater interface...')

if __name__ == "__main__":
    sys.exit(main())
