""" Convert, edit, and save streams """

from pydub import AudioSegment
import os

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

        recording = AudioSegment.from_wav(self.sourcefile_path)
        recording.export(
            self.mp3file_path,
            bitrate=self.bitrate,
            format="mp3",
            tags={
                'artist': self.performer,
                'album': self.album,
                'title': self.title
                },
            cover=self.cover_path
            )

        return print("Converted " + self.sourcefile_path + " to " + self.mp3file_path)