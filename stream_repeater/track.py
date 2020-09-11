""" Handling for individual tracks """

class Track(object):
    def __init__(self, artist, title, track_file, index_time):
        self.artist = artist
        self.index_time = index_time
        self.title = title
        self.track_file = track_file

    def __artist(self, s):
        self.artist = s

    def __index_time(self, s):
        self.index_time = s

    def __title(self, s):
        self.title = s

    def __track_file(self, s):
        self.track_file = s