# Snowsky Echo Mini File Processor

- [Snowsky Echo Mini File Processor](#snowsky-echo-mini-file-processor)
  - [Why?](#why)
  - [Issues This Addresses](#issues-this-addresses)
    - [Track names](#track-names)
    - [Track order](#track-order)
    - [Multiple discs](#multiple-discs)
  - [Supported Filetypes](#supported-filetypes)
  - [Setting up](#setting-up)
  - [Running](#running)


An opinionated tool to organize files on a Snowsky Echo Mini device.

## Why?

The Snowsky Echo Mini is a low cost DAP with a lot to like about it, however it
has some limitations which can be awkward to work with.

## Issues This Addresses

### Track names

Although the Echo Mini uses a database track names are still displayed using
their filename instead of the track name tag.

To work around this the file is renamed to
`${track_number} - ${track_title}.${file_extension}`. i.e. `01 - My Song.flac`.

### Track order

The Echo Mini appears to use the track number tag for the album order, however
it does not seem to support tags also containing the total number of tracks
(i.e. `2/13`).

To work around this the total tracks is removed from the track number. The
number is also padded to 2 characters. I.e. `2` and `2/13` will both become
`02`.

### Multiple discs

Albums consisting of more than one disc are not ordered by the disc number.

To work around this the album name is updated to include the disc number. I.e.
`My Album` would become `My Album (disc 1)` and `My Album (disc 2)`.

## Supported Filetypes

Currently only MP3 and FLAC files are supported.

## Setting up

This has been tested in macOS and Linux with [WSL for Windows](
https://learn.microsoft.com/en-us/windows/wsl/install).

```
git clone https://github.com/ntr0n/echo-mini-file-processor.git
cd echo-mini-file-processor
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
```

## Running

**Note:** this process does permanently change the files. It also does so in a
way that is opinionated as to how the Echo Mini handles files. Therefore it is
recommended to either run this directly on the files on the device or create a
backup first. Never run this on the only copy of your library.

The program contains a single file as an input.

```shell
python3 process_file.py /path/to/my/file.mp3
```

It can be combined with `find` to work across multiple files.

```shell
find /path/to/my/mini -name '*.mp3' -exec \
    python3 process_file.py {} \;
```
