
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description ='Lists duplicate files found by scan.py')

parser.add_argument('--hashes', dest='hashes', action='store', default='hashes',
                    help='Path to store hashes.')
args = parser.parse_args()

def printLine(line:str):
  (hash, size, filename) = line.split(' ', 2)
  print(size + ' ' + filename.strip())

basepath = args.hashes
for (root,dirs,files) in os.walk(basepath):
  for file in files:
    with open(Path(basepath, file), "r") as f:
      lines = f.readlines()
      lines.sort()
      prevLine = ''
      prevHash = ''
      prevIsPrinted = False
      for line in lines:
        (hash, size, filename) = line.split(" ", 2)
        if (hash == prevHash):
          if (not prevIsPrinted):
            print()
            printLine(prevLine)
            prevIsPrinted = True
          printLine(line)
        else:
          prevIsPrinted = False
          prevLine = line
          prevHash = hash