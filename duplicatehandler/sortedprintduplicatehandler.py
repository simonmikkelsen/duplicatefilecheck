from duplicatehandler.duplicatehandler import DuplicateHandler
from model.duplicateset import DuplicateSet

class SortedPrintDuplicateHanler(DuplicateHandler):

  def __init__(self) -> None:
    super().__init__()
    self.duplicates = {}

  def handleDuplicate(self, hash:str, size:int, file:str):
    if hash in self.duplicates:
      self.duplicates[hash].addFile(file)
    else:
      set = DuplicateSet(hash, size)
      set.addFile(file)
      self.duplicates[hash] = set
    
  def finished(self):
    # todo: Can someone print a sorted version effectively of the values without duplicating the entire dataset?
    sets = list(self.duplicates.values())
    sets.sort(key=lambda s: int(s.size))
    for s in sets:
      for file in s.getFiles():
        print(f'{s.getSize()} {file.strip()}')
