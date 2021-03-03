""" Handling for individual tracks """

class Track(object):
    def __init__(self, performer, title, track_filename, track_number, index_time):
        self.index_time = index_time
        self.performer = performer
        self.title = title
        self.track_filename = track_filename
        self.track_number = track_number

    def __index_time(self, s):
        self.index_time = s

    def __performer(self, s):
        self.performer = s

    def __title(self, s):
        self.title = s

    def __track_filename(self, s):
        self.track_filename = s

    def __track_number(self, s):
        self.track_number = s