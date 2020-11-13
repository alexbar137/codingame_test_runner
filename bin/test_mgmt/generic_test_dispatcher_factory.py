from bin.interfaces.dispathcer_factory_interface import DispatcherFactoryInterface

from bin.file_helpers.line_by_line_file_reader import LineByLineFileReader
from bin.file_helpers.generic_file_saver import GenericFileSaver
from bin.file_helpers.coding_game_file_loader import CodingGameFileLoader
from bin.test_mgmt.generic_test_dispatcher import GenericTestDispatcher


class GenericTestDispatcherFactory(DispatcherFactoryInterface):
  def __init__(self, base_dir: str):
    super(GenericTestDispatcherFactory, self).__init__()
    self.BASE_DIR = base_dir

  def get_dispatcher(self) -> GenericTestDispatcher:
    options = {
      "file_loader": CodingGameFileLoader(),
      "file_reader": LineByLineFileReader(),
      "file_saver": GenericFileSaver(self.BASE_DIR),
      "base_dir": self.BASE_DIR
    }
    return GenericTestDispatcher(options)