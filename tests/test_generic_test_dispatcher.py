from unittest import TestCase
from unittest.mock import patch, MagicMock

from bin.interfaces.file_saver_interface import FileSaverInterface
from bin.interfaces.file_reader_interface import FileReaderInterface
from bin.interfaces.file_loader_interface import FileLoaderInterface

from bin.test_mgmt.generic_test_dispatcher import GenericTestDispatcher


class TestGenericTestDispatcher(TestCase):

  @patch.multiple(FileLoaderInterface, __abstractmethods__=set())
  @patch.multiple(FileReaderInterface, __abstractmethods__=set())
  @patch.multiple(FileSaverInterface, __abstractmethods__=set())
  def setUp(self) -> None:
    options = {
      "file_loader": FileLoaderInterface(),
      "file_reader": FileReaderInterface(),
      "file_saver": FileSaverInterface()
    }
    self.test_cases = [
      ["first", "second", "third"],
      ["fourth", "fifth", "sixth"],
      ["seventh", "eighth", "ninth"]
    ]
    self.test_dispatcher = GenericTestDispatcher(options)

  def test_get_puzzles_online(self):
    self.test_dispatcher.FILE_READER.file_exists = MagicMock(False)
    self.test_dispatcher.FILE_SAVER.save_in_file = MagicMock()

    for test_case in self.test_cases:
      self.test_dispatcher.FILE_LOADER.load_file = MagicMock(test_case)
      self.assertEqual(test_case, self.test_dispatcher.get_puzzle("test_name", "test_id"))
      self.test_dispatcher.FILE_SAVER.save_in_file.assert_called_with("test_name", test_case)

  def test_get_expected_results_online(self):
    self.test_dispatcher.FILE_READER.file_exists = MagicMock(False)
    self.test_dispatcher.FILE_SAVER.save_out_file = MagicMock()

    for test_case in self.test_cases:
      self.test_dispatcher.FILE_LOADER.load_file = MagicMock(test_case)
      self.assertEqual(test_case, self.test_dispatcher.get_expected_results("test_name", "test_id"))
      self.test_dispatcher.FILE_SAVER.save_out_file.assert_called_with("test_name", test_case)


  def test_file_dispatching_local(self):
    self.test_dispatcher.FILE_READER.file_exists = MagicMock(True)
    self.test_dispatcher.FILE_SAVER.save_in_file = MagicMock()
    self.test_dispatcher.FILE_SAVER.save_out_file = MagicMock()

    for test_case in self.test_cases:
      self.test_dispatcher.FILE_READER.read_file = MagicMock(test_case)
      self.assertEqual(test_case, self.test_dispatcher.get_puzzle("test", "test"))
      self.assertEqual(test_case, self.test_dispatcher.get_expected_results("test", "test"))
      self.test_dispatcher.FILE_SAVER.save_in_file.assert_not_called()
      self.test_dispatcher.FILE_SAVER.save_out_file.assert_not_called()
