""" Processing for CUE sheets """

if __package__:
    from .track import Track
else:
    from track import Track
import os, sys, re
import datetime, time, math

class CueSheet(object):
    """ CUE sheet-handling Object """

    def __init__(self, options):
        self.cuesheet = options['stream']['cuesheet']
        self.datadir = options['system']['datadir']
        self.in_header = True

        # These are the placeholders for retrieved info
        self.date = ''
        self.filename = ''
        self.genre = ''
        self.index = ''
        self.performer = ''
        self.recorded_by = ''
        self.title = ''
        self.track_number = ''

        # Collection of header information retrieved and individual Tracks
        self.header = dict()
        self.tracks = list()

        # Build the matching engine for the CUE sheet
        self.regex_lst = (
			(re.compile(r'FILE\s(.+)\sWAVE'), self.__filename),
			(re.compile(r'INDEX\s(\d{2})\s(\d{1,3}:\d{2}:\d{2})'), self.__index),
			(re.compile(r'PERFORMER\s(.+)'), self.__performer),
			(re.compile(r'REM DATE\s(.+)'), self.__date),
			(re.compile(r'REM GENRE\s(.+)'), self.__genre),
            (re.compile(r'REM RECORDED_BY\s(.+)'), self.__recorded_by),
			(re.compile(r'TITLE\s(.+)'), self.__title),
			(re.compile(r'TRACK\s(\d{2})\sAUDIO'), self.__track_number)
		)

    def __date(self, s):
        self.date = s

    def __filename(self, s):
        if self.in_header:
            self.header['filename'] = s
        else:
            self.filename = s

    def __genre(self, s):
        self.genre = s

    def __index(self, s):
        self.index = s
    
    def __index(self, idx, s):
        """ Handler for when the index number and time string are given """

        self.index = self.index_time(s)

    def __performer(self, s):
        if self.in_header:
            self.header['performer'] = s
        else:
            self.performer = s

    def __recorded_by(self, s):
        self.recorded_by = s

    def __reset_track_attr(self):
        """ Reset the values track-related attributes """

        self.filename = ''
        self.index = ''
        self.performer = ''
        self.title = ''
        self.track_number = ''

    def __title(self, s):
        if self.in_header:
            self.header['title'] = s
        else:
            self.performer = s
        self.title = s

    def __track_number(self, s):
        """ Handler for tracks. If a new track is found it will commit
            all currently recorded information into a Track as well as
            keep track of being in a header """

        # If no Tracks have been recorded then we're out of the header
        if self.in_header:
            self.in_header = False
            self.track_number = s
        # We have loaded all info for a previous track and are ready to commit
        else:
            self.commit_track()
            self.__reset_track_attr()
            self.track_number = s

    def commit_track(self):
        """ Add a Track to the list of discovered tracks """

        self.tracks.append( Track(self.performer, self.title, self.filename, self.track_number, self.index) )

    @staticmethod
    def dqstrip(s):
        if s[0] == '"' and s[-1] == '"': return s[1:-1]
        return s

    @staticmethod
    def index_time(s):
        """ Returns the time of the indexed track in seconds"""

        x = time.strptime(s,'%H:%M:%S')
        time_in_seconds = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        return time_in_seconds

    @staticmethod
    def unquote(t):
        return tuple([CueSheet.dqstrip(s.strip()) for s in t])

    def csv(self):
        """ Convert a CUE sheet to CSV """

        print("CSV conversion not supported yet")

    def dump(self):
        """ Dump the loaded CUE sheet """

        for key in self.header:
            print(str(key) + ": " + str(self.header[key]))
        for idx, val in enumerate(self.tracks):
            print("Track No: " + str(idx))
            print("  Artist: " + str(val.performer))
            print("  Title: " + str(val.title))
            print("  Index Time: " + str(val.index_time))
            print("  Filename: " + str(val.track_filename))

    def load(self):
        """ Load all tracks and information from a CUE sheet into memory """

        cuesheet_file_path = self.datadir + "/" + self.cuesheet
        header = True
        new_track = False

        # Loop over each line of the CUE sheet
        for line in open(cuesheet_file_path):
            for regex, handler in self.regex_lst:
                match_result = regex.match(line.strip())
                if match_result:
                    handler(*self.unquote(match_result.groups()))

        # Commit the last track
        self.commit_track()
        self.__reset_track_attr()
