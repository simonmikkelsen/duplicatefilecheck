from pathlib import Path

from hashedfilehandler.hashedfilehandler import HashedFileHandler
from hashedfilehandler.utils.filehashwriter import FileHashWriter

class HashedFileWriter(HashedFileHandler):

  def __init__(self, basepath:Path) -> None:
    self.basepath = basepath
    self.writer = FileHashWriter(Path(basepath))

  def directory(self, dir:Path) -> None:
    pass

  def hash(self, file:Path, filesize:int, hash:str, levelOfPath = -1) -> None:
    self.writer.persistHash(hash, file, filesize)

  def newRootPath(self) -> None:
    pass

  def finish(self) -> None:
    pass
