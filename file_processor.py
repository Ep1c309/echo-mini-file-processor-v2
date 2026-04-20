from base_file import BaseAudioFile
import os
import re

class FileProcessor:
    def __init__(self, audio_file: BaseAudioFile, dry_run: bool):
        self.audio_file = audio_file
        self.dry_run = dry_run

    def process(self):
        print('Processing {}'.format(self.audio_file.fullpath))

        self.__processTags()
        self.__renameFile()

    def __processTags(self) -> None:
        self.__set_track_number()
        self.__set_disc_to_album_tag()

        if not self.dry_run:
            self.audio_file.save_tags()

    def __renameFile(self) -> None:
        filename = self.__build_filename()

        if self.dry_run:
            print('Renaming file to {}'.format(filename))
            return
        
        dirname = os.path.dirname(self.audio_file.fullpath)
        os.rename(self.audio_file.fullpath, '{}/{}'.format(dirname, filename))

    def __set_track_number(self) -> None:
        track_number = self.audio_file.get_track()

        if self.dry_run:
            print('Set track number to {}'.format(track_number))
        
        self.audio_file.set_track(track_number)

    def __set_disc_to_album_tag(self) -> None:
        disc_number = self.audio_file.get_disc()

        if disc_number is None:
            return
        
        if self.__album_name_contains_disc_number(disc_number):
            return
        
        new_album = '{} (disc {})'.format(
            self.audio_file.get_album(),
            disc_number
        )
        
        if self.dry_run:
            print('Set album to {}'.format(new_album))
            return

        self.audio_file.set_album(new_album)
        
    def __album_name_contains_disc_number(self, disc_number) -> bool:
        album_name = self.audio_file.get_album()

        candidates = [
            'disc {}',
            'Disc {}',
            'CD {}',
        ]

        for candidate in candidates:
            if candidate.format(disc_number) in album_name:
                return True
            
        return False
    
    def __build_filename(self) -> str:
        return '{} - {}{}'.format(
            self.audio_file.get_track(),
            re.sub(r'[?/\\]', '', self.audio_file.get_title()),
            self.audio_file.file_extension
        )
