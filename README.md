# Spaceless filenamer

Sniff through specified directory and rename the files to no longer
have spaces or parentheses.

## Usage

    $ python3 spaceless.py -i /path/to/directory/with/files


### Squashing dates

If the filename starts with a date in the form of
**YYYY-MM-DD-rest-of-filename.jpg** then there is an option to squash
that into **YYYYMMDD-rest-of-filename.jpg**

    $ python3 spaceless.py -i /path/to/directory -d true


## Requirements

- Python 3

## License

Released under [BSD 3-Clause](./LICENSE).
