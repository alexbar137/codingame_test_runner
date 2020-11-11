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
    failing_constructor = lambda: GenericFileSaver("wrong path")
    self.assertRaises(FileExistsError, failing_constructor)

  def test_constructor_folders_created(self):
    file_saver = GenericFileSaver(self.BASE_DIR)
    self.assertTrue(os.path.exists(self.IN_PATH), "IN dir is not created")
    self.assertTrue(os.path.exists(self.OUT_PATH), "OUT dir is not created")

  def test_save_out_file(self):
    content = ["abc", "def", "ghi"]
    name = "test_out"
    expected_location = self.OUT_PATH + "/" + name
    file_saver = GenericFileSaver(self.BASE_DIR)
    file_saver.save_out_file(name, content)
    self.assertTrue(os.path.exists(expected_location), "OUT file is not saved")
    with open(expected_location) as f:
      strings = f.readlines()
      self.assertEqual(content[1], strings[1].strip())

  def test_save_in_file(self):
    content = ["abc", "def", "ghi"]
    name = "test_in"
    expected_location = self.IN_PATH + "/" + name
    file_saver = GenericFileSaver(self.BASE_DIR)
    file_saver.save_in_file(name, content)
    self.assertTrue(os.path.exists(expected_location), "IN file is not saved")
    with open(expected_location) as f:
      strings = f.readlines()
      self.assertEqual(content[1], strings[1].strip())
