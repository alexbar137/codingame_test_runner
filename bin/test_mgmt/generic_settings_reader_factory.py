from bin.test_mgmt.generic_settings_reader import GenericSettingsReader

from bin.file_helpers.json_test_case_reader import JsonTestCaseReader
from bin.file_helpers.yaml_config_reader import YamlConfigReader

from bin.interfaces.settings_reader_factory_interface import SettingsReaderFactoryInterface

class GenericSettingsReaderFactory(SettingsReaderFactoryInterface):
  def get_settings_reader(self) -> GenericSettingsReader:
    options = {
      "config_reader": YamlConfigReader(),
      "test_case_reader": JsonTestCaseReader()
    }
    return GenericSettingsReader(options)