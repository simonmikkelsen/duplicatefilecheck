import hashlib
import os
from pathlib import Path

class BlockFileHash:
  def __init__(self, blockSize: int, blockCount: int) -> None:
    self.blockSize = blockSize
    self.blockCount = blockCount

  def __md5(self, fname: Path) -> str:
    hash_md5 = hashlib.md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

  def __md5Parts(self, stat: os.stat_result, filePath: Path) -> str:
      hash_md5 = hashlib.md5()
      fileSize = stat.st_size
      readBlockStartOffset = int(round(fileSize / self.blockCount))
      readChunk = min(4096, self.blockSize)
      with open(filePath, "rb") as f:
        for startOffset in range(0, fileSize, readBlockStartOffset):
            f.seek(startOffset)
            readThisTime = 0
            # todo: This could make sure we don't read too much, but isn't it better to just have properly sized chinks?
            # amountToRead = min(readChunk, self.blockSize - readThisTime)
            for chunk in iter(lambda: f.read(readChunk), b''):
                #todo: This will read the whole readChunk even if it ends up reading more than blockSize. 
                hash_md5.update(chunk)
                readThisTime += readChunk
                if (readThisTime >= self.blockSize):
                  break # Break the inner for loop
      return hash_md5.hexdigest()

  def __getHashCodeAllFile(self, path: Path) -> str:
    return self.__md5(path)

  def __getHashCodeForBlocks(self, stat: os.stat_result, path: Path) -> str:
    return self.__md5Parts(self.blockSize, self.blockCount, stat, path)

  def getHashcode(self, path: Path) -> str:
    stat = path.stat()
    if (stat.st_size <= self.blockSize * self.blockCount):
      return self.__getHashCodeAllFile(path)
    else:
      return self.__getHashCodeForBlocks(self.blockSize, self.blockCount, stat, path)
