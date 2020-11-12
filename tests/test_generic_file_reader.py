import unittest
from bin.file_helpers.generic_file_reader import GenericFileReader


class FileLoaderTestCase(unittest.TestCase):
  def setUp(self):
    self.BASE_DIR = "../tests/test_files"
    self.CORRECT_IN_PATH = "../tests/test_files/in/coefficients.txt"
    self.CORRECT_OUT_PATH = "../tests/test_files/out/coefficients.txt"
    self.file_loader = GenericFileReader()
    self.file_exists_test_cases = {
        self.CORRECT_IN_PATH: True,
        "../tests/test_files/in/coefficients1.txt": False,
        "coefficients1.txt": False
      }
    self.load_file_test_cases = [
      (self.CORRECT_IN_PATH, 0, "7"),
      (self.CORRECT_IN_PATH, 7, "ADD $2 $5"),
      (self.CORRECT_OUT_PATH, 0, "10"),
      (self.CORRECT_OUT_PATH, 6, "38")
    ]

  def test_file_exists(self):
    for test_case in self.file_exists_test_cases:
      self.assertEqual(self.file_exists_test_cases[test_case],
                       self.file_loader.file_exists(test_case),
                       test_case)

  def test_read_file(self):
    for test_case in self.load_file_test_cases:
      (file_path, string_number, string_content) = test_case
      strings = self.file_loader.read_file(file_path)
      self.assertEqual(string_content, strings[string_number],"{0}: {1}".format(file_path, string_number))

if __name__ == '__main__':
  unittest.main()
