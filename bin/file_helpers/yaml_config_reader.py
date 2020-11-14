from bin.interfaces.file_reader_interface import FileReaderInterface
from bin.test_mgmt.settings_constants import SettingsConstants
import yaml
from typing import Dict

class YamlConfigReader(FileReaderInterface):
  def __init__(self):
    super(YamlConfigReader, self).__init__()

  def read_file(self, path: str):
    with open(path) as f:
      settings = yaml.load(f, Loader=yaml.FullLoader)
      self._validate_settings(settings)
      return settings

  @staticmethod
  def _validate_settings(settings: Dict):
    if SettingsConstants.BASE_DIR_NAME not in settings or SettingsConstants.TEST_CASES not in settings:
      raise IndexError("No required settings in config")



