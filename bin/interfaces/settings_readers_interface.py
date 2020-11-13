from abc import ABC, abstractmethod
from typing import Dict

from bin.interfaces.file_reader_interface import FileReaderInterface

class SettingsReaderInterface(ABC):
  def __init__(self, options: str):
    super(SettingsReaderInterface, self).__init__()
    self.SETTINGS_PATH: str = options["settings_path"]
    self.CONFIG_READER: FileReaderInterface  = options["config_reader"]
    self.TEST_CASE_READER: FileReaderInterface = options["test_case_reader"]

  @abstractmethod
  def get_test_cases_path(self) -> Dict:
    pass

  @abstractmethod
  def get_test_cases(self) -> Dict:
    pass