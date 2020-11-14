from typing import Dict

from bin.interfaces.settings_reader_interface import SettingsReaderInterface
from bin.test_mgmt.settings_constants import SettingsConstants

class GenericSettingsReader(SettingsReaderInterface):
  def __init__(self, options: Dict):
    super(GenericSettingsReader, self).__init__(options)
    self.SETTINGS = self.CONFIG_READER.read_file(SettingsConstants.SETTINGS_PATH)
    self.TEST_CASES = self.TEST_CASE_READER.read_file(self.SETTINGS[SettingsConstants.TEST_CASES])

  def get_base_dir(self) -> str:
    return self.SETTINGS[SettingsConstants.BASE_DIR_NAME]

  def get_test_cases(self) -> Dict:
    return self.TEST_CASES
