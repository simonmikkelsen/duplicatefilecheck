import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description ='''Takes a file generated by list.py and removes non existing files.
As long as no spaces are added you can write charaters before the path in the file.''')

parser.add_argument('--in', '-i', dest='ins', action='store',
                    help='File containing filenames (in Unix format) from list.py.')
args = parser.parse_args()

inFile = args.ins
with open(Path(inFile), 'r') as f:
  lines = f.readlines()
  for line in lines:
    (pre, filename) = line.split(' ', 1)
    filepath = Path(filename.strip())
    if filepath.exists():
      print(pre + ' ' + filename.strip())
