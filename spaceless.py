from argparse import ArgumentParser
from pathlib import Path
import re
import os

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input_dir",
    required=True,
    help="/path/to/directory")
parser.add_argument("-d", "--date", dest="reformat_date",
    default=False,
    help="/path/to/directory")
args = parser.parse_args()


def rename_dateformat(filename):
    date_pattern = "^([0-9]{4})-([0-9]{2})-([0-9]{2})(.*)"

    if re.match(date_pattern, filename):
        filename = re.sub(date_pattern, "\\1\\2\\3\\4", filename)

    return filename


def rename_without_junk(filename):
    clean = filename.replace(' ', '-')
    clean = re.sub('[\(\)]', '', clean)

    return clean


try:
    if not os.path.exists(args.input_dir):
        print("Cannot open directory: " + args.input_dir)
        exit(1)

    for filename in os.listdir(args.input_dir):
        clean_filename = rename_without_junk(filename)

        if args.reformat_date:
            clean_filename = rename_dateformat(clean_filename)

        clean_filepath = args.input_dir + clean_filename

        if filename == clean_filename:
            continue

        if Path(clean_filepath).is_file():
            continue

        os.rename(args.input_dir + filename, clean_filepath)
        print("{} -> {}".format(filename, clean_filename))

except FileNotFoundError:
    print("Cannot open directory: " + args.input_dir)
