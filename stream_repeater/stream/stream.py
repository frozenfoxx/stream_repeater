""" Convert, edit, and save streams """

import re
import os
import subprocess

DUR_REGEX = re.compile(
    r"Duration: (?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d{2})\.(?P<ms>\d{2})"
)
TIME_REGEX = re.compile(
    r"out_time=(?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d{2})\.(?P<ms>\d{2})"
)

def to_ms(s=None, des=None, **kwargs) -> float:
    if s:
        hour = int(s[0:2])
        minute = int(s[3:5])
        sec = int(s[6:8])
        ms = int(s[10:11])
    else:
        hour = int(kwargs.get("hour", 0))
        minute = int(kwargs.get("min", 0))
        sec = int(kwargs.get("sec", 0))
        ms = int(kwargs.get("ms", 0))

    result = (hour * 60 * 60 * 1000) + (minute * 60 * 1000) + (sec * 1000) + ms
    if des and isinstance(des, int):
        return round(result, des)
    return result

class Stream(object):
    """ Stream-handling Object """

    def __init__(self, options):
        self.album = options['stream']['album']
        self.bitrate = options['stream']['bitrate']
        self.cover = options['stream']['cover']
        self.datadir = options['system']['datadir']
        self.performer = options['stream']['performer']
        self.sourcefile = options['stream']['sourcefile']
        self.tags = options['stream']['tags']
        self.title = options['stream']['title']

        # Check if a cuesheet was supplied
        if 'cuesheet' in options['stream']:
            self.cuesheet = options['stream']['cuesheet']
        else:
            self.cuesheet = ''

        # Check if a historysheet was supplied
        if 'historysheet' in options['stream']:
            self.historysheet = options['stream']['historysheet']
        else:
            self.historysheet = ''

        # Check if a mp3file was supplied
        if 'mp3file' in options['stream']:
            self.mp3file = options['stream']['mp3file']
        else:
            self.mp3file = os.path.splitext(self.sourcefile)[0] + ".mp3"

        # Set file pathing
        self.cover_path = self.datadir + "/" + self.cover
        self.mp3file_path = self.datadir + "/" + self.mp3file
        self.sourcefile_path = self.datadir + "/" + self.sourcefile

        print("Stream initialized")

    def conversion_run(self, cmd):
        """ Run a conversion command """

        total_dur = None

        print("Running the following command: " + cmd)

        with subprocess.Popen(cmd,
            shell=True,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True) as p:
            for line in p.stdout:
                #DEBUG: print(line, end='')
                if not total_dur and DUR_REGEX.search(line):
                    total_dur = DUR_REGEX.search(line).groupdict()
                    total_dur = to_ms(**total_dur)
                    continue
                if total_dur:
                    result = TIME_REGEX.search(line)
                    if result:
                        elapsed_time = to_ms(**result.groupdict())
                        yield int(elapsed_time / total_dur * 100)

        if p.returncode != 0:
            raise subprocess.CalledProcessError(p.returncode, p.args)

    def convert_to_mp3(self):
        """ Convert a recording to MP3 """

        # Check if it has already been converted
        if os.path.exists(self.mp3file_path):
            print("MP3 file already exists at " + self.mp3file_path)
            return "data: 100"

        print("MP3 file not found, converting to MP3")

        # Build the command prefix
        command = ["ffmpeg", "-progress", "-", "-nostats"]

        # Add the sourcefile
        command.extend(["-i", "\"" + self.sourcefile_path + "\""])

        # Add cover art
        command.extend(["-i", "\"" + self.cover_path + "\""])

        # Add the number of channels
        command.extend(["-ac", "2"])

        # Add the sampling frequency
        command.extend(["-ar", "44100"])

        # Add the format
        command.extend(["-f", "mp3"])

        # Add the desired bitrate
        command.extend(["-b:a", self.bitrate])

        # Add ID3v2 tags
        command.extend(["-write_id3v2", "1",
            "-metadata", "artist=\"" + self.performer + "\"",
            "-metadata", "album=\"" + self.album + "\"",
            "-metadata", "title=\"" + self.title + "\""])

        # Add the mp3file_path output
        command.append("\"" + self.mp3file_path + "\"")

        try:
            for i in self.conversion_run(" ".join(command)):
                #DEBUG: print("Percentage converted: " + str(i))
                yield "data: " + str(i) + "\n\n"
        except:
            print("Failed to convert " + self.sourcefile_path + " to " + self.mp3file_path)
            yield "data: -1"
