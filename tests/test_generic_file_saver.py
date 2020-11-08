from unittest import TestCase
import shutil
import os

from bin.file_helpers.generic_file_saver import GenericFileSaver


class TestGenericFileSaver(TestCase):
  def setUp(self) -> None:
    self.BASE_DIR = "../tests/test_files/saver"
    self.IN_PATH = self.BASE_DIR + "/in"
    self.OUT_PATH = self.BASE_DIR + "/out"

  def tearDown(self) -> None:
    if os.path.exists(self.IN_PATH):
      shutil.rmtree(self.IN_PATH)
    if os.path.exists(self.OUT_PATH):
      shutil.rmtree(self.OUT_PATH)

  def test_constructor_exception(self):
    f = lambda: GenericFileSaver("wrong path")
    self.assertRaises(FileExistsError, f)

  def test_constructor_folders_created(self):
    file_saver = GenericFileSaver(self.BASE_DIR)
    self.assertTrue(os.path.exists(self.IN_PATH))
    self.assertTrue(os.path.exists(self.OUT_PATH))
