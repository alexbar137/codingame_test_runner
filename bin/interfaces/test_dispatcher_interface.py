from abc import ABC, abstractmethod
from typing import List, Dict
from bin.interfaces.file_saver_interface import FileSaverInterface
from bin.interfaces.file_loader_interface import FileLoaderInterface
from bin.interfaces.file_reader_interface import FileReaderInterface

class TestDispatcherInterface(ABC):
  def __init__(self, options: List[Dict]):
    super().__init__()
    self.FILE_LOADER: FileLoaderInterface = options["file_loader"]
    self.FILE_SAVER: FileSaverInterface = options["file_saver"]
    self.FILE_READER: FileReaderInterface = options["file_reader"]


  @abstractmethod
  def get_puzzle(self, name: str, file_id: str):
    pass

  @abstractmethod
  def get_expected_results(self, name: str, file_id: str):
    pass