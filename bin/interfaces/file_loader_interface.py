from abc import ABC, abstractmethod
from typing import List

class FileLoaderInterface (ABC):
  def __init__(self):
    super().__init__()

  @abstractmethod
  def load_file(self, file_id: str) -> List[str]:
    pass