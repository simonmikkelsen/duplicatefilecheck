import argparse
import os
from pathlib import Path

#from duplicatehandler.duplicatehandler import PrintDuplicateHandler
from duplicatehandler.sortedprintduplicatehandler import SortedPrintDuplicateHanler

parser = argparse.ArgumentParser(description ='Lists duplicate files found by scan.py')

parser.add_argument('--hashes', dest='hashes', action='store', default='hashes',
                    help='Path to store hashes.')
args = parser.parse_args()

def printLine(line:str):
  (hash, size, filename) = line.split(' ', 2)
  print(size + ' ' + filename.strip())

#duplicateHandlers = [PrintDuplicateHandler()]
duplicateHandlers = [SortedPrintDuplicateHanler()]

basepath = args.hashes
for (root,dirs,files) in os.walk(basepath):
  for file in files:
    with open(Path(basepath, file), "r") as f:
      lines = f.readlines()
      lines.sort()
      (prevHash, prevSize, prevFilename) = ('', '', '')
      prevIsHandled = False
      for line in lines:
        (hash, size, filename) = line.split(" ", 2)
        if (hash == prevHash):
          if (not prevIsHandled):
            [handler.handleDuplicate(prevHash, prevSize, prevFilename) for handler in duplicateHandlers]
            prevIsHandled = True
          [handler.handleDuplicate(hash, size, filename) for handler in duplicateHandlers]
        else:
          prevIsHandled = False
          (prevHash, prevSize, prevFilename) = (hash, size, filename)
[handler.finished() for handler in duplicateHandlers]