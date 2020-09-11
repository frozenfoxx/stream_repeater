""" Convert, edit, and save streams """

import os
import sys
from pydub import AudioSegment

class Stream(object):
    """ Stream-handling Object """

    def __init__(self, options):
        self.album = options['stream']['album']
        self.bitrate = options['stream']['bitrate']
        self.cover = options['stream']['cover']
        self.cuesheet = options['stream']['cuesheet']
        self.datadir = options['system']['datadir']
        self.filename = options['stream']['filename']
        self.performer = options['stream']['performer']
        self.title = options['stream']['title']

    def convert_to_mp3(self):
        """ Convert a recording to MP3 """

        stream_file_path = self.datadir + "/" + self.filename
        cover_file_path = self.datadir + "/" + self.cover

        recording = AudioSegment.from_wav(stream_file_path)
        mp3_filename = os.path.splitext(stream_file_path)[0] + ".mp3"
        recording.export(
            mp3_filename,
            bitrate=self.bitrate,
            format="mp3",
            tags={
                'artist': self.performer,
                'album': self.album,
                'title': self.title
                },
            cover=cover_file_path
            )
            
        print("Converted " + stream_file_path + " to " + mp3_filename)