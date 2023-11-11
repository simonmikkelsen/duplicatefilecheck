from abc import ABC, abstractmethod

class DuplicateHandler(ABC):
  @abstractmethod
  def handleDuplicate(self, hash:str, size:int, file:str):
      pass
  
  @abstractmethod
  def finished(self):
     pass