import os
from pathlib import Path

from filehash import FileHash

blockSize = 200*1024
blockCount = 2

filehash = FileHash(blockSize, blockCount)
# Travers all the branch of a specified path, bottom first
for (root,dirs,files) in os.walk('.',topdown=False):
  for file in files:
    path = Path(root, file)
    if (path.is_file()):
      hash = filehash.getHashcode(blockSize, blockCount, path)
      print(hash + ' ' + str(path.absolute()))

