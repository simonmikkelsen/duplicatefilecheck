from duplicatehandler.duplicatehandler import DuplicateHandler

class PrintDuplicateHanler(DuplicateHandler):

  def __init__(self) -> None:
    super().__init__()
    self.prevHash = ''

  def handleDuplicate(self, hash:str, size:int, file:str):
    if self.prevHash != hash:
      print()
      self.prevHash = hash
    print(f'{size} {file}')
    
  def finished(self):
     pass