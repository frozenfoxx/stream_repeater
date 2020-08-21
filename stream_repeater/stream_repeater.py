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

    options = Options().load_options()
    prompt = Prompt(options)
    prompt.prompt = 'stream_repeater> '
    prompt.cmdloop('[+] Starting stream_repeater interface...')

if __name__ == "__main__":
    sys.exit(main())
