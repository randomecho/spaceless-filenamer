from argparse import ArgumentParser
from pathlib import Path
import re
import os

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input_dir",
    required=True,
    help="/path/to/directory")
args = parser.parse_args()


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
        clean_filepath = args.input_dir + clean_filename

        if filename == clean_filename:
            continue

        if Path(clean_filepath).is_file():
            continue

        os.rename(args.input_dir + filename, clean_filepath)
        print("{} -> {}".format(filename, clean_filename))

except FileNotFoundError:
    print("Cannot open directory: " + args.input_dir)
