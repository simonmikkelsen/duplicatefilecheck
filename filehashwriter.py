from os import stat_result
from pathlib import Path

class FileHashWriter:
    def __init__(self, basePath: Path) -> None:
        self.basePath = basePath
        self.basePath.mkdir(parents=True, exist_ok=True)

    def persistHash(self, hash:str, filePath: Path, stat:stat_result) -> None:
        firstChars = hash[0:2]
        with open(Path(self.basePath, firstChars + '.txt'), 'a') as f:
            f.write(hash)
            f.write(' ')
            f.write(str(stat.st_size))
            f.write(' ')
            f.write(str(filePath.absolute()))
            f.write('\n')
