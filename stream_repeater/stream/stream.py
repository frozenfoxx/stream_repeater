""" Convert, edit, and save streams """

import os
import subprocess

class Stream(object):
    """ Stream-handling Object """

    def __init__(self, options):
        self.album = options['stream']['album']
        self.bitrate = options['stream']['bitrate']
        self.cover = options['stream']['cover']
        self.datadir = options['system']['datadir']
        self.performer = options['stream']['performer']
        self.sourcefile = options['stream']['sourcefile']
        self.tags = options['stream']['tags']
        self.title = options['stream']['title']

        # Check if a cuesheet was supplied
        if 'cuesheet' in options['stream']:
            self.cuesheet = options['stream']['cuesheet']
        else:
            self.cuesheet = ''

        # Check if a historysheet was supplied
        if 'historysheet' in options['stream']:
            self.historysheet = options['stream']['historysheet']
        else:
            self.historysheet = ''

        # Check if a mp3file was supplied
        if 'mp3file' in options['stream']:
            self.mp3file = options['stream']['mp3file']
        else:
            self.mp3file = os.path.splitext(self.sourcefile)[0] + ".mp3"

        # Set file pathing
        self.cover_path = self.datadir + "/" + self.cover
        self.mp3file_path = self.datadir + "/" + self.mp3file
        self.sourcefile_path = self.datadir + "/" + self.sourcefile

        print("Stream initialized")

    def convert_to_mp3(self):
        """ Convert a recording to MP3 """

        # Check if it has already been converted
        if os.path.exists(self.mp3file_path):
            return print("MP3 file already exists at " + self.mp3file_path)

        print("MP3 file not found, converting to MP3")

        # Build the command prefix
        command = ["ffmpeg", "-v", "warning", "-hide_banner", "-stats"]

        # Add the sourcefile
        command.extend(["-i", "\"" + self.sourcefile_path + "\""])

        # Add cover art
        command.extend(["-i", "\"" + self.cover_path + "\""])

        # Add the number of channels
        command.extend(["-ac", "2"])

        # Add the sampling frequency
        command.extend(["-ar", "44100"])

        # Add the format
        command.extend(["-f", "mp3"])

        # Add the desired bitrate
        command.extend(["-b:a", self.bitrate])

        # Add ID3v2 tags
        command.extend(["-write_id3v2", "1",
            "-metadata", "artist=\"" + self.performer + "\"",
            "-metadata", "album=\"" + self.album + "\"",
            "-metadata", "title=\"" + self.title + "\""])

        # Add the mp3file_path output
        command.append("\"" + self.mp3file_path + "\"")

        print("Running the following command: " + " ".join(command))

        try:
            subprocess.run(" ".join(command), shell=True, check=True)
            return print("Converted " + self.sourcefile_path + " to " + self.mp3file_path)
        except:
            return print("Failed to convert " + self.sourcefile_path + " to " + self.mp3file_path)
