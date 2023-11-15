from abc import ABC, abstractmethod
from pathlib import Path

class HashedFileHandler(ABC):
  @abstractmethod
  def directory(self, dir:Path) -> None:
    pass

  @abstractmethod
  def hash(self, file:Path, filesize:int, hash:str, levelOfPath = -1) -> None:
    pass

  @abstractmethod
  def newRootPath(self) -> None:
    pass
