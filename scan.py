import hashlib
import os
from pathlib import Path
import argparse

from blockfilehash import BlockFileHash
from hashedfilehandler.directoryhandler import DirectoryHandler
from hashedfilehandler.hashfilewriter import HashedFileWriter

parser = argparse.ArgumentParser(description ='Index files to find duplicates.')
 
parser.add_argument('-p', '--path', dest ='path', 
                    action ='append',
                    default = [], help ='Paths to index. Specify multiple times for more paths.')
parser.add_argument('--hashes', dest='hashes', action='store', default='hashes.txt',
                    help='File to store hashes. The specified folder must exist.')
parser.add_argument('-m', '--min-size', dest='minsize', action='store', default='1',
                    help='Minimum file size to hash. Default 1 byte (ignore empty files). Postfix with k, m, g, t, e, p, e, z or y for KiB, MiB, GiB etc.')
parser.add_argument('-n', '--naive', dest='naive', action='store_true', default=False,
                    help='When given files that should be ignored due to size are hashed based on their file size and name (without path). '
                    'This allows for a reasonable detection of duplicate directories, just much faster.')
args = parser.parse_args()

blockSize = 50*4096
blockCount = 2
hashFilePath = Path(args.hashes)
naive:bool = args.naive

if len(args.path) > 0:
  pathList = args.path
else:
  pathList = ['.']

def sizeToInt(size: str) -> int:
  if (size.isnumeric()):
    return int(size)
  # A dictionary that maps the letters to their corresponding values
  letter_values = {"k": 1024, "m": 1024**2, "g": 1024**3, "t": 1024**4, "p": 1024**5, "e": 1024**6, "z": 1024*7, "y": 1024**8}
  # Split the string into the number and the letter parts
  number = float(size[:-1])
  letter = size[-1].lower()
  if letter not in letter_values:
    raise ValueError("Invalid size postfix: " + letter)
  # Multiply the number by the value of the letter and return it as an integer
  return int(number * letter_values[letter])

minSize = sizeToInt(args.minsize)
filehash = BlockFileHash(blockSize, blockCount)

hashedFileWriter = HashedFileWriter(hashFilePath)
filehandlers = [hashedFileWriter, DirectoryHandler(hashedFileWriter)]

for indexpath in pathList:
  [ handler.newRootPath() for handler in filehandlers ]
  for root, dirs, files in os.walk(indexpath, topdown=True):
    dirs.sort() #Ensure we always traverse dirs in the same order.
    [ handler.directory(Path(root)) for handler in filehandlers ]
    for file in files:
      path = Path(root, file)
      try:
        if (not path.is_file()):
          continue
        stat = path.stat()
        if (stat.st_size >= minSize):
          hash = filehash.getHashcode(path)
          [ handler.hash(path, stat.st_size, hash) for handler in filehandlers ]
          print(hash + ' ' + str(path.absolute()))
        elif naive:
          hash = filehash.getNaiveHashcode(path, stat.st_size)
          [ handler.hash(path, stat.st_size, hash) for handler in filehandlers ]

      except PermissionError as e:
        # todo: Handle more errors and put them in a separate log file.
        print('Ignore ' + str(path) + ': ' + str(e))
      except UnicodeEncodeError as e:
        #print('Ignore ' + str(path) + ' (unicode): ' + str(e))
        pass
[ handler.finish() for handler in filehandlers ]
