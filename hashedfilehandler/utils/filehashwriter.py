from pathlib import Path

class FileHashWriter:
    def __init__(self, hashFilePath: Path) -> None:
        self.fp = open(Path(hashFilePath), 'a')

    def persistHash(self, hash:str, filePath: Path, filesize:int) -> None:
        try:
          self.fp.write(hash)
          self.fp.write(' ')
          self.fp.write(str(filesize))
          self.fp.write(' ')
          self.fp.write(str(filePath.absolute()))
          self.fp.write('\n')
        except UnicodeEncodeError as e:
          # Todo handle properly.
          #print('Ignore ' + str(filePath.) + ' (unicode): ' + str(e))
          pass
