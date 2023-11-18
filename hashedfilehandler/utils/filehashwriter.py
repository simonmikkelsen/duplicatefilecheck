from pathlib import Path

class FileHashWriter:
    def __init__(self, basePath: Path) -> None:
        self.basePath = basePath
        self.basePath.mkdir(parents=True, exist_ok=True)

    def persistHash(self, hash:str, filePath: Path, filesize:int) -> None:
        firstChars = hash[0:2]
        try:
          with open(Path(self.basePath, firstChars + '.txt'), 'a') as f:
              f.write(hash)
              f.write(' ')
              f.write(str(filesize))
              f.write(' ')
              f.write(str(filePath.absolute()))
              f.write('\n')
        except UnicodeEncodeError as e:
          # Todo handle properly.
          #print('Ignore ' + str(filePath.) + ' (unicode): ' + str(e))
          pass
