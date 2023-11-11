
class DuplicateSet:
  def __init__(self, hash:str, size:int) -> None:
    self.hash = hash
    self.size = size
    self.files = []

  def getHash(self) -> str:
    return self.hash
  def getSize(self) -> int:
    return self.size
  def getFiles(self):
    return self.files
  def addFile(self, file):
    self.files.append(file)