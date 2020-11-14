from unittest import TestCase
from unittest import TestCase

from bin.file_helpers.json_test_case_reader import JsonTestCaseReader


class TestJsonTestCaseReader(TestCase):
  def setUp(self) -> None:
    self.TEST_CASES_PATH = "../tests/test_files/json_reader/tests_cases.json"
    self.WRONG_TEST_CASES_PATH = "../tests/test_files/json_reader/tests_cases.py"
    self.WRONG_TEST_CASE = "../tests/test_files/json_reader/wrong.json"
    self.WRONG_STRUCTURE = {
      "test_cases": "wrong"
    }
    self.test_case_reader = JsonTestCaseReader()
    self.TEST_CASES = [
      {
        "puzzle_id": 41772404133258,
        "expected_results_id": 41772422311279,
        "label": "Simple dependency"
      },
      {
        "puzzle_id": 41772444718621,
        "expected_results_id": 41772467277639,
        "label": "Double dependency"
      },
      {
        "puzzle_id": 41772489349199,
        "expected_results_id": 41772508356088,
        "label": "Subtraction"
      },
      {
        "puzzle_id": 41772525003896,
        "expected_results_id": 41772545372472,
        "label": "Multiplication"
      },
      {
        "puzzle_id": 41772564771716,
        "expected_results_id": 41772585694481,
        "label": "No dependencies"
      },
      {
        "puzzle_id": 41772606068533,
        "expected_results_id": 41772628381741,
        "label": "Coefficients"
      },
      {
        "puzzle_id": 41772645410669,
        "expected_results_id": 41772663434043,
        "label": "Fibonacci"
      },
      {
        "puzzle_id": 41772681759223,
        "expected_results_id": 41772702591728,
        "label": "Backward dependency"
      },
      {
        "puzzle_id": 41772720188863,
        "expected_results_id": 41772749931847,
        "label": "Diamond dependency"
      },
      {
        "puzzle_id": 41772762281572,
        "expected_results_id": 41772789158820,
        "label": "Accounting is easy"
      },
      {
        "puzzle_id": 41772805348154,
        "expected_results_id": 41772829395385,
        "label": "Accounting is hard 1"
      },
      {
        "puzzle_id": 41772842882802,
        "expected_results_id": 41772867025162,
        "label": "Accounting is hard 2"
      },
      {
        "puzzle_id": 41772885804611,
        "expected_results_id": 41772907988256,
        "label": "Deep Birecursion"
      }
    ]

  def test_read_file(self):
    results = self.test_case_reader.read_file(self.TEST_CASES_PATH)
    self.assertEqual(self.TEST_CASES, results)

  def test_wrong_file_extension(self):
    f = lambda: self.test_case_reader.read_file(self.WRONG_TEST_CASES_PATH)
    self.assertRaises(Exception, f)

  def test__validate_file_content(self):
    f = lambda : self.test_case_reader._validate_file_content(self.WRONG_STRUCTURE)
    self.assertRaises(Exception, f)

  def test_wrong_file_structure(self):
    f = lambda : self.test_case_reader.read_file(self.WRONG_TEST_CASE)
    self.assertRaises(Exception, f)
