""" Handling for individual tracks """

class Track(object):
    def __init__(self, artist, title, track_file, start_time):
        self.artist = artist
        self.start_time = start_time
        self.title = title
        self.track_file = track_file
