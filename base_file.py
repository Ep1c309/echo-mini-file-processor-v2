import os

class BaseAudioFile:
    def __init__(self, fullpath: str, mutagen):
        self.filename, self.file_extension = os.path.splitext(fullpath)
        self.fullpath = fullpath
        self.mutagen = mutagen

    def get_title(self) -> str:
        if not 'title' in self.mutagen:
            raise Exception('Title is not present')
        
        return self.mutagen['title'][0]
    
    def get_track(self) -> str:
        if not 'tracknumber' in self.mutagen:
            raise Exception('Track number is not present')

        track_number_string = self.mutagen['tracknumber'][0]

        if '/' in track_number_string:
            track_number, track_total = track_number_string.split('/')
        else:
            track_number = track_number_string
        
        return f'{int(track_number):02}'
    
    def get_album(self) -> str:
        if not 'album' in self.mutagen:
            raise Exception('Album is not present')
        
        return self.mutagen['album'][0]
    
    def get_disc(self) -> int | None:
        disc_number_tag = self._get_tag('discnumber')
        disc_total_tag = self._get_tag('disctotal')

        if disc_number_tag is not None and '/' in disc_number_tag:
            # Format is 1/2, disc total is stored in disc number
            disc_number_string, disc_total_string = disc_number_tag.split('/')
        else:
            disc_number_string = disc_number_tag
            disc_total_string = disc_total_tag
        
        if disc_number_string is None:
            return None
        
        disc_number_int = int(disc_number_string)

        # If disc is more than 1 we know we want to use it.
        # Accounts for when total is not set.
        if disc_number_int > 1:
            return disc_number_int
        
        # Bail if we can't determine the disc or if there is only 1
        if disc_total_string is None:
            return None
        
        disc_total_int = int(disc_total_string)

        if disc_total_int < 2:
            return None

        # Disc is part of a set
        return disc_number_int
    
    def set_track(self, track) -> None:
        self.mutagen['tracknumber'] = [track]

    def set_album(self, album) -> None:
        self.mutagen['album'] = [album]
    
    def save_tags(self) -> None:
        self.mutagen.save()

    def _get_tag(self, tag_name) -> str | None:
        if not tag_name in self.mutagen:
            return None

        return self.mutagen[tag_name][0]
