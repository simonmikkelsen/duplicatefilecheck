import os
from pathlib import Path

from blockfilehash import BlockFileHash

blockSize = 200*1024
blockCount = 2

filehash = BlockFileHash(blockSize, blockCount)

# Travers all the branch of a specified path, bottom first
for (root,dirs,files) in os.walk('.',topdown=False):
  for file in files:
    path = Path(root, file)
    if (path.is_file()):
      hash = filehash.getHashcode(path)
      print(hash + ' ' + str(path.absolute()))
