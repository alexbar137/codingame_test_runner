from abc import ABC, abstractmethod
from typing import List

class FileReaderInterface (ABC):
  def __init__(self):
    super().__init__()

  @abstractmethod
  def read_file(self, path: str) -> List[str]:
    pass