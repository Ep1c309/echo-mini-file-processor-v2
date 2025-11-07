from base_file import BaseAudioFile
from mutagen.flac import FLAC

class FLACAudioFile(BaseAudioFile):
    def __init__(self, fullpath):
        mutagen = FLAC(fullpath)

        super().__init__(fullpath, mutagen)
