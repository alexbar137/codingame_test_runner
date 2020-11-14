from abc import ABC, abstractmethod
from bin.interfaces.settings_reader_interface import SettingsReaderInterface

class SettingsReaderFactoryInterface(ABC):
  def __init__(self):
    super(SettingsReaderFactoryInterface, self).__init__()

  @abstractmethod
  def get_settings_reader(self) -> SettingsReaderInterface:
    pass