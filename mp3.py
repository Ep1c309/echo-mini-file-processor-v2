from base_file import BaseAudioFile
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

class MP3AudioFile(BaseAudioFile):
    def __init__(self, fullpath):
        mutagen = MP3(fullpath, ID3=EasyID3)

        super().__init__(fullpath, mutagen)
