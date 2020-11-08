from unittest import TestCase, skip
from bin.file_helpers.coding_game_file_loader import CodingGameFileLoader

class TestCodingGameFileLoader(TestCase):
  def setUp(self):
    self.load_file_test_cases = {
      "41772606068533": "7",
      "41772628381741": "10",
      "41772564771716": "3",
      "41772585694481": "3"
    }
    self.file_loader = CodingGameFileLoader()

  @skip("CodingGameFileLoader: Avoid API excessive load")
  def test_load_file(self):
    for test_case in self.load_file_test_cases:
      self.assertEqual(self.load_file_test_cases[test_case],
                       self.file_loader.load_file(test_case)[0],
                       test_case)
