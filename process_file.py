import argparse
from file_processor import FileProcessor
import flac
import mp3
import os

parser = argparse.ArgumentParser(
                    prog='echo-mini-file-processor',
                    description='Renames and tags audio file for Snowsky Echo Mini')

parser.add_argument('filename')
parser.add_argument('--dry-run', action='store_true')

args = parser.parse_args()

filename, file_extension = os.path.splitext(args.filename)

if file_extension == '.mp3':
    audio_file = mp3.MP3AudioFile(args.filename)
elif file_extension == '.flac':
    audio_file = flac.FLACAudioFile(args.filename)
else:
    raise Exception('Unsupported filetype {}'.format(file_extension))

file_processor = FileProcessor(audio_file, args.dry_run)
file_processor.process()
