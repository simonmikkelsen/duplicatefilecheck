import os
from pathlib import Path

from blockfilehash import BlockFileHash
from filehashwriter import FileHashWriter

blockSize = 200*1024
blockCount = 2
basepath = 'hashes'

filehash = BlockFileHash(blockSize, blockCount)
writer = FileHashWriter(Path(basepath))

# Travers all the branch of a specified path, bottom first
for (root,dirs,files) in os.walk('.',topdown=False):
  for file in files:
    path = Path(root, file)
    if (path.is_file()):
      hash = filehash.getHashcode(path)
      writer.persistHash(hash, path)
      print(hash + ' ' + str(path.absolute()))
