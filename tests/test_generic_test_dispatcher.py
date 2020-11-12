from unittest import TestCase
from unittest.mock import patch, MagicMock
import os.path

from bin.interfaces.file_saver_interface import FileSaverInterface
from bin.interfaces.file_reader_interface import FileReaderInterface
from bin.interfaces.file_loader_interface import FileLoaderInterface

from bin.test_mgmt.generic_test_dispatcher import GenericTestDispatcher


class TestGenericTestDispatcher(TestCase):

  @patch.multiple(FileLoaderInterface, __abstractmethods__=set())
  @patch.multiple(FileReaderInterface, __abstractmethods__=set())
  @patch.multiple(FileSaverInterface, __abstractmethods__=set())
  def setUp(self) -> None:
    current_dir = os.path.dirname(__file__)
    base_dir = os.path.join(current_dir, "test_files", "dispatcher")
    options = {
      "file_loader": FileLoaderInterface(),
      "file_reader": FileReaderInterface(),
      "file_saver": FileSaverInterface(),
      "base_dir": base_dir
    }
    self.test_cases = [
      ["first", "second", "third"],
      ["fourth", "fifth", "sixth"],
      ["seventh", "eighth", "ninth"]
    ]
    self.test_dispatcher = GenericTestDispatcher(options)

  @patch('os.path.exists')
  def test_get_puzzles_online(self, mock_exists):
    mock_exists.return_value = False
    self.test_dispatcher.FILE_SAVER.save_in_file = MagicMock()
    self.test_dispatcher.FILE_SAVER.save_out_file = MagicMock()

    for test_case in self.test_cases:
      self.test_dispatcher.FILE_LOADER.load_file = MagicMock(return_value=test_case)
      self.assertEqual(test_case, self.test_dispatcher.get_puzzle("test_name", "test_id"))
      self.test_dispatcher.FILE_SAVER.save_in_file.assert_called_with("test_name", test_case)
      self.test_dispatcher.FILE_SAVER.save_out_file.assert_not_called()

  @patch('os.path.exists')
  def test_get_expected_results_online(self, mock_exists):
    mock_exists.return_value = False
    self.test_dispatcher.FILE_SAVER.save_out_file = MagicMock()
    self.test_dispatcher.FILE_SAVER.save_in_file = MagicMock()

    for test_case in self.test_cases:
      self.test_dispatcher.FILE_LOADER.load_file = MagicMock(return_value=test_case)
      self.assertEqual(test_case, self.test_dispatcher.get_expected_results("test_name", "test_id"))
      self.test_dispatcher.FILE_SAVER.save_out_file.assert_called_with("test_name", test_case)
      self.test_dispatcher.FILE_SAVER.save_in_file.assert_not_called()

  @patch('os.path.exists')
  def test_file_dispatching_local(self, mock_exists):
    mock_exists.return_value = True
    self.test_dispatcher.FILE_SAVER.save_in_file = MagicMock()
    self.test_dispatcher.FILE_SAVER.save_out_file = MagicMock()

    for test_case in self.test_cases:
      self.test_dispatcher.FILE_READER.read_file = MagicMock(return_value=test_case)
      self.assertEqual(test_case, self.test_dispatcher.get_puzzle("test", "test"))
      self.assertEqual(test_case, self.test_dispatcher.get_expected_results("test", "test"))
      self.test_dispatcher.FILE_SAVER.save_in_file.assert_not_called()
      self.test_dispatcher.FILE_SAVER.save_out_file.assert_not_called()

  def test_get_path_from_name(self):
    test_cases = [
      ("i_exist.txt", "IN", True),
      ("i_exist.txt", "OUT", True)
    ]

    for test_case in test_cases:
      file_name, file_type, expected_result = test_case
      file_path = self.test_dispatcher._get_path_from_name(file_name, file_type)
      self.assertEqual(expected_result, os.path.exists(file_path))

  def test_get_path_from_name_exception(self):
    f = lambda : self.test_dispatcher._get_path_from_name("test", "wrong")
    self.assertRaises(Exception,f)

  def test_ad_base_dir_exception(self):
    f = lambda : self.test_dispatcher._add_base_dir("/wrong/base/dir")
    self.assertRaises(Exception, f)