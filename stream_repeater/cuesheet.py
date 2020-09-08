""" Processing for CUE sheets """

if __package__:
    from .track import Track
else:
    from track import Track
import os, sys, re
import time, math

class CueSheet(object):
    """ CUE sheet-handling Object """

    def __init__(self, options):
        self.datadir = options['system']['datadir']
        self.date = ''
        self.file = ''
        self.genre = ''
        self.index = ''
        self.performer = ''
        self.cuesheet = options['stream']['cuesheet']
        self.title = ''
        self.tracks = []

        self.regex_lst = (
			(re.compile(r'PERFORMER\s(.+)'), self.__performer),
			(re.compile(r'REM DATE\s(.+)'), self.__date),
			(re.compile(r'REM GENRE\s(.+)'), self.__genre),
			(re.compile(r'TITLE\s(.+)'), self.__title),
			(re.compile(r'FILE\s(.+)\sWAVE'), self.__file),
			(re.compile(r'TRACK\s(\d{2})\sAUDIO'), self.__track),
			(re.compile(r'INDEX\s(\d{2})\s(\d{1,3}:\d{2}:\d{2})'), self.__index)
		)

    def __date(self, s):
        self.date = s

    def __file(self, s):
        self.file = s

    def __genre(self, s):
        self.genre = s

    def __performer(self, s):
        if not self.tracks:
            self.performer = s
        else:
            self.tracks[-1].performer = s

    def __title(self, s):
        if not self.tracks:
            self.title = s
        else:
            self.tracks[-1].title = s

    def __track(self, s):
        self.track = s

    @staticmethod
    def dqstrip(s):
        if s[0] == '"' and s[-1] == '"': return s[1:-1]
        return s

    @staticmethod
    def index_split(s):
        t = s.split(':')
        return (int(t[0])*60 + int(t[1]))*75 + int(t[2])

    @staticmethod
    def unquote(t):
        return tuple([CueSheet.dqstrip(s.strip()) for s in t])

    def __index(self, idx, s):
        idx = int(idx)
        self.tracks[-1].time[idx] = self.index_split(s)

    def csv(self):
        """ Convert a CUE sheet to CSV """

        print("CSV conversion not supported yet")

    def read(self):
        cuesheet_file_path = self.datadir + "/" + self.cuesheet

        for line in open(cuesheet_file_path):
            for regex, handler in self.regex_lst:
                match_result = regex.match(line.strip())
                if match_result:
                    handler(*self.unquote(match_result.groups()))
            self.tracks.append( Track(self.__performer, self.__title, self.__file, self.__index) )

