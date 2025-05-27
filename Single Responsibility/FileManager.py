from pathlib import Path
import os

class FileManger:
    def __init__(self, filename):
        self.path = Path(filename)
    
    def read(self, encoding = 'utf-8'):
        return self.path.read_text(encoding)

    def write(self, data, encoding = 'utf-8'):
        self.path.write_text(data, encoding)
