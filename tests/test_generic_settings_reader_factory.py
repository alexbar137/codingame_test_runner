from unittest import TestCase
from unittest.mock import patch
from bin.test_mgmt.generic_settings_reader import GenericSettingsReader
from bin.test_mgmt.generic_settings_reader_factory import GenericSettingsReaderFactory


class TestGenericSettingsReaderFactory(TestCase):

  @patch('bin.file_helpers.json_test_case_reader.JsonTestCaseReader', return_value=None)
  @patch('bin.file_helpers.yaml_config_reader.YamlConfigReader', return_value=None)
  @patch('bin.test_mgmt.generic_settings_reader.GenericSettingsReader.__init__', return_value=None)
  def test_get_settings_reader(self, mock_json, mock_yaml, mock_settings_reader):
    factory = GenericSettingsReaderFactory()
    self.assertIsInstance(factory.get_settings_reader(), GenericSettingsReader)
