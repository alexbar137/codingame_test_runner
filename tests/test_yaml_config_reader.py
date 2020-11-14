from unittest import TestCase
from bin.file_helpers.yaml_config_reader import YamlConfigReader
from bin.test_mgmt.settings_constants import SettingsConstants


class TestYamlConfigReader(TestCase):
  def setUp(self) -> None:
    self.SETTINGS_PATH = "../tests/test_files/yaml_reader/config.yaml"
    self.config_reader = YamlConfigReader()
    self.WRONG_SETTINGS = [
      {"test_cases": "test_cases"},
      {"base_dir": "base_dir"}
    ]

  def test_read_file(self):
    settings = self.config_reader.read_file(self.SETTINGS_PATH)
    self.assertEqual("test base dir", settings[SettingsConstants.BASE_DIR_NAME])
    self.assertEqual("test cases path", settings[SettingsConstants.TEST_CASES])

  def test_validate_settings(self):
    for test_case in self.WRONG_SETTINGS:
      f = lambda : self.config_reader._validate_settings(test_case)
      self.assertRaises(IndexError, f)
