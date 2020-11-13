from typing import Dict

from bin.interfaces.settings_readers_interface import SettingsReaderInterface

class GenericSettingsReader(SettingsReaderInterface):

  def get_test_cases_path(self) -> Dict:
    pass

  def get_test_cases(self) -> Dict:
    pass
