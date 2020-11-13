from unittest import TestCase
from unittest.mock import patch
from bin.test_mgmt.generic_test_dispatcher_factory import GenericTestDispatcherFactory
from bin.test_mgmt.generic_test_dispatcher import GenericTestDispatcher


class TestGenericTestDispatcherFactory(TestCase):

  @patch('bin.file_helpers.line_by_line_file_reader.LineByLineFileReader.__init__', return_value=None)
  @patch('bin.file_helpers.generic_file_saver.GenericFileSaver.__init__', return_value=None)
  @patch('bin.file_helpers.coding_game_file_loader.CodingGameFileLoader.__init__', return_value=None)
  @patch('bin.test_mgmt.generic_test_dispatcher.GenericTestDispatcher.__init__', return_value=None)
  def test_get_dispatcher(self, mock_file_reader, mock_file_saver, mock_file_loader, mock_test_dispatcher):
    factory = GenericTestDispatcherFactory("test")
    dispatcher = factory.get_dispatcher()
    self.assertIsInstance(dispatcher, GenericTestDispatcher)
