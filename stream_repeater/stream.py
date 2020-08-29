""" Convert, edit, and save streams """

import os
import sys
from pydub import AudioSegment

class Stream(object):
    """ Stream-handling Object """

    def __init__(self, options):
        self.options = options

    def convert_to_mp3(self):
        """ Convert a recording to MP3 """

        filename = self.options['system']['datadir'] + "/" + self.options['stream']['filename']
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
            
        print("Converted " + filename + " to " + mp3_filename)