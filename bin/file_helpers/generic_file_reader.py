from typing import List
from bin.interfaces.file_reader_interface import FileReaderInterface
from os import path


class GenericFileReader(FileReaderInterface):
  def read_file(self, file_path: str) -> List[str]:
    with open(file_path) as f:
      content = f.readlines()
      content = [x.strip() for x in content]
      return  content

