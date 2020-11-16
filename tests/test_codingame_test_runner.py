from unittest import TestCase
from unittest import TestCase
from unittest.mock import patch, MagicMock
from bin.test_mgmt.generic_settings_reader import GenericSettingsReader
from codingame_test_runner import CodingameTestRunner
from bin.test_mgmt.generic_settings_reader_factory import GenericSettingsReaderFactory
from bin.file_helpers.json_test_case_reader import JsonTestCaseReader


class TestCodingameTestRunner(TestCase):

  def setUp(self) -> None:
    self.BASE_DIR = "../tests/test_files/test_runner"
    self.TEST_CASES_PATH = "../tests/test_files/test_runner/prefix-code.json"
    json_reader = JsonTestCaseReader()
    self.TEST_CASES = json_reader.read_file(self.TEST_CASES_PATH)
    mock_settings_reader = MagicMock(type=GenericSettingsReader)
    mock_settings_reader.get_base_dir = MagicMock(return_value=self.BASE_DIR)
    mock_settings_reader.get_test_cases = MagicMock(return_value=self.TEST_CASES)

    with patch.object(GenericSettingsReaderFactory,
                      "get_settings_reader",
                      return_value=mock_settings_reader):
      self.test_runner = CodingameTestRunner()

  def test_constructor(self):
    self.assertEqual(self.BASE_DIR, self.test_runner.BASE_DIR)
    self.assertEqual(self.TEST_CASES, self.test_runner.TEST_CASES)

  def test_get_puzzle(self):
    test_cases = [
      {
        "id": 8,
        "content": [
          "6",
          "1 32",
          "001 67",
          "0100 85",
          "000 72",
          "0101 10",
          "011 79",
          "00100100100110001100010110110110111010011010010010010010011000110000101001111100011000101111011101001101001001111100011000010100111110000000000001011110111010011010010011111000000000000010100111110001100010111101110100110100100111110001100001010010010010011000110001011011011011101000100010001001001001001001100011000"
        ]
      },
      {
        "id": 6,
        "content": [
          "0",
          "01111100001010000001011010000011111100000011111011100101010000010100"
        ]
      }
    ]

    for test_case in test_cases:
      puzzle = self.test_runner.get_puzzle(test_case["id"])
      self.assertEqual(test_case["content"], puzzle)

  def test_get_expected_results(self):
    test_cases = [
      {
        "id": 6,
        "content": [
          "DECODE FAIL AT INDEX 0"
        ]
      },
      {
        "id": 8,
        "content": [
          "CCCC H  H OOOO U  U CCCC H  H",
          "C    H  H O  O U  U C    H  H",
          "C    HHHH O  O U  U C    HHHH",
          "C    H  H O  O U  U C    H  H",
          "CCCC H  H OOOO UUUU CCCC H  H"
        ]
      }
    ]

    for test_case in test_cases:
      result = self.test_runner.get_expected_results(test_case["id"])
      self.assertEqual(test_case["content"], result)

  def test_get_test_cases(self):
    test_cases = [
      {
        "id": 1,
        "content": {
          "puzzle": [
            "9",
            "011 32",
            "0011 33",
            "0010 114",
            "0001 100",
            "0000 101",
            "111 87",
            "110 72",
            "10 108",
            "010 111",
            "1100000101001001111101000101000010110011"
          ],
          "expected_results": [
            "Hello World !"
          ],
          "label": "HelloWorld"
        }
      },
      {
        "id": 0,
        "content": {
          "puzzle": [
            "5",
            "1 97",
            "001 98",
            "000 114",
            "011 99",
            "010 100",
            "10010001011101010010001"
          ],
          "expected_results": [
            "abracadabra"
          ],
          "label": "abracadabra"
        }
      },
    ]
    actual = self.test_runner.get_test_cases()
    for test_case in test_cases:
      self.assertEqual(test_case["content"], actual[test_case["id"]])