""" Convert, edit, and save streams """

import os
import sys
from pydub import AudioSegment

class Stream(object):
    """ Stream-handling Object """

    def __init__(self, options):
        self.album = options['stream']['album']
        self.artist = options['stream']['artist']
        self.bitrate = options['stream']['bitrate']
        self.cover = options['stream']['cover']
        self.datadir = options['system']['datadir']
        self.filename = options['stream']['filename']
        self.title = options['stream']['title']

    def convert_to_mp3(self):
        """ Convert a recording to MP3 """

        filepath = self.datadir + "/" + self.filename
        recording = AudioSegment.from_wav(filepath)
        mp3_filename = os.path.splitext(filepath)[0] + ".mp3"
        recording.export(
            mp3_filename,
            bitrate=self.bitrate,
            format="mp3",
            tags={
                'artist': self.artist,
                'album': self.album,
                'title': self.title
                },
            cover=self.cover
            )
            
        print("Converted " + filepath + " to " + mp3_filename)