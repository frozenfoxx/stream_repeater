""" Convert, edit, and save streams """

import os
from pydub import AudioSegment

class Stream(object):
    """ Stream-handling Object """

    def __init__(self, options):
        print("Stream initialized")
        self.album = options['stream']['album']
        self.bitrate = options['stream']['bitrate']
        self.cover = options['stream']['cover']
        self.cuesheet = options['stream']['cuesheet']
        self.datadir = options['system']['datadir']
        self.filename = options['stream']['filename']
        self.historysheet = options['stream']['historysheet']
        self.performer = options['stream']['performer']
        self.tags = options['stream']['tags']
        self.title = options['stream']['title']

        self.cover_path = self.datadir + "/" + self.cover
        self.file_path = self.datadir + "/" + self.filename
        self.mp3_path = ''

    def convert_to_mp3(self):
        """ Convert a recording to MP3 """

        print("Converting to MP3")

        recording = AudioSegment.from_wav(self.file_path)
        self.mp3_path = os.path.splitext(self.file_path)[0] + ".mp3"
        recording.export(
            self.mp3_path,
            bitrate=self.bitrate,
            format="mp3",
            tags={
                'artist': self.performer,
                'album': self.album,
                'title': self.title
                },
            cover=self.cover_path
            )

        return print("Converted " + self.file_path + " to " + self.mp3_path)