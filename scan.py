import os
from pathlib import Path
import argparse

from blockfilehash import BlockFileHash
from filehashwriter import FileHashWriter

parser = argparse.ArgumentParser(description ='Index files to find duplicates.')
 
parser.add_argument('-p', '--path', dest ='path', 
                    action ='append',
                    default = [], help ='Paths to index. Specify multiple times for more paths.')
parser.add_argument('--hashes', dest='hashes', action='store', default='hashes',
                    help='Path to store hashes.')
args = parser.parse_args()

blockSize = 200*1024
blockCount = 2
basepath = args.hashes

filehash = BlockFileHash(blockSize, blockCount)
writer = FileHashWriter(Path(basepath))

# Travers all the branch of a specified path, bottom first
for indexpath in args.path:
  for (root,dirs,files) in os.walk(indexpath, topdown=False):
    for file in files:
      path = Path(root, file)
      if (path.is_file()):
        hash = filehash.getHashcode(path)
        writer.persistHash(hash, path)
        print(hash + ' ' + str(path.absolute()))
