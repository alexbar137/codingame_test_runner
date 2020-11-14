from unittest import TestCase
from unittest.mock import patch, MagicMock
from bin.interfaces.file_reader_interface import FileReaderInterface

from bin.test_mgmt.generic_settings_reader import GenericSettingsReader


class TestGenericSettingsReader(TestCase):

  @patch.multiple(FileReaderInterface, __abstractmethods__=set())
  def setUp(self) -> None:
    self.CORRECT_BASE_DIR = "correct base dir"
    self.CORRECT_TEST_CASES = [
      {
        "index": 1,
        "inputBinaryId": 41772404133258,
        "outputBinaryId": 41772422311279,
        "label": "Simple dependency"
      },
      {
        "index": 2,
        "inputBinaryId": 41772444718621,
        "outputBinaryId": 41772467277639,
        "label": "Double dependency"
      },
      {
        "index": 3,
        "inputBinaryId": 41772489349199,
        "outputBinaryId": 41772508356088,
        "label": "Subtraction"
      }
    ]
    mock_config_reader = FileReaderInterface()
    mock_config_reader.read_file = MagicMock(return_value={
      "base_dir": self.CORRECT_BASE_DIR,
      "test_cases": "test"
    })

    mock_test_case_reader = FileReaderInterface()
    mock_test_case_reader.read_file = MagicMock(return_value=self.CORRECT_TEST_CASES)
    options = {
      "config_reader": mock_config_reader,
      "test_case_reader": mock_test_case_reader
    }
    self.settings_reader = GenericSettingsReader(options)

  def test_get_base_dir(self):
    self.assertEqual(self.CORRECT_BASE_DIR, self.settings_reader.get_base_dir())

  def test_get_test_cases(self):
    self.assertEqual(self.CORRECT_TEST_CASES, self.settings_reader.get_test_cases())
