import hashlib
from pathlib import Path

from hashedfilehandler.hashedfilehandler import HashedFileHandler

class DirectoryHandler(HashedFileHandler):
  def __init__(self, writer:HashedFileHandler) -> None:
    self.newRootPath()
    self.writer = writer

  def newRootPath(self) -> None:
    self.hash_md5 = hashlib.md5()
    self.child = None
    self.level = -1
    self.path = None
    self.totalSize = 0

  def directory(self, dir:Path, levelOfPath = -1) -> None:
    if levelOfPath != -1:
      level = levelOfPath
      # Assume that dir is resolved() if called with levelOfPath set.
    else:
      level = self.__calculate_level(dir)
      dir = dir.resolve()

    if self.path == None:
      # First time the method is called
      self.level = level
      self.path = dir
    elif self.level + 1 == level:
      # A new sub directory of ours is called: Replace our child.
      if self.child != None:
        self.child.finish()
      self.child = DirectoryHandler(self.writer)
      self.child.directory(dir, level)
    elif level > self.level:
      # When a new sub directory is called
      self.child.directory(dir, level)
    elif self.level == level:
      # Directory on the same level as us: I.e. a new dir. This should never happen.
      raise BaseException('This should never happen. New child on same level as previous: ' + str(self.path) + '; ' + str(dir))
    else:
      raise 'This else should never happen'
      # Todo remove all these raise

  def __calculate_level(self, dir:Path) -> int:
    return len(dir.parts)
  
  def hash(self, file:Path, filesize:int, hash:str) -> None:
    self.hash_md5.update(hash.encode())
    self.totalSize += filesize
    if self.child != None:
      self.child.hash(file, filesize, hash)

  def finish(self):
    self.writer.hash(self.path, self.totalSize, self.hash_md5.hexdigest())
