from pathlib import Path
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input_dir",
    required=True,
    help="/path/to/directory")
args = parser.parse_args()


def rename_without_junk(filename):
    return filename.replace(' ', '-')


try:
    if not os.path.exists(args.input_dir):
        print("Cannot open directory: " + args.input_dir)
        exit(1)

    for filename in os.listdir(args.input_dir):
        if ' ' not in filename:
            continue

        clean_filename = rename_without_junk(filename)
        clean_filepath = args.input_dir + clean_filename

        if Path(clean_filepath).is_file():
            continue

        os.rename(args.input_dir + filename, clean_filepath)
        print("{} -> {}".format(filename, clean_filename))

except FileNotFoundError:
    print("Cannot open directory: " + args.input_dir)
