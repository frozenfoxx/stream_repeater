""" Processing for history sheet """

if __package__:
    from .track import Track
else:
    from track import Track
import csv

class HistorySheet(object):
    """ History sheet-handling Object """

    def __init__(self, options):
        self.datadir = options['system']['datadir']
        self.historysheet = options['stream']['historysheet']
        self.tracks = dict()

    def dump(self):
        """ Dump the loaded History sheet """

        for idx, val in enumerate(self.tracks):
            print("Track No: " + str(val.track_number))
            print("  Artist: " + str(val.performer))
            print("  Title: " + str(val.title))
            print("  Index Time: " + str(val.index_time))
            print("  Filename: " + str(val.track_filename))

    def load(self):
        """ Load all tracks and information from a History sheet into memory """

        historysheet_file_path = self.datadir + "/" + self.historysheet

        with open(historysheet_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')
            for row in reader:
                self.tracks.append( Track(row['Artist'], row['Track Title'], "Not Supported", row['#'], row['Time']) )
