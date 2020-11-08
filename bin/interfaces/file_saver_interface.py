from abc import ABC, abstractmethod
from typing import List

class FileSaverInterface(ABC):
  def __init__(self):
    super().__init__()

  @abstractmethod
  def save_in_file(self, name: str, content: List[str]) -> None:
    pass

  @abstractmethod
  def save_out_file(self, name: str, content: List[str]) -> None:
    pass