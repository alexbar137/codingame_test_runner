from bin.interfaces.test_dispatcher_interface import TestDispatcherInterface
from os import path

class GenericTestDispatcher(TestDispatcherInterface):
  FOLDERS = {
    "OUT": "out",
    "IN": "in"
  }

  def __init__(self, options):
    super(GenericTestDispatcher, self).__init__(options)
    self._add_base_dir(options["base_dir"])

  def get_puzzle(self, name: str, file_id: str):
    return self.__dispatch_files(name, file_id, "IN")

  def get_expected_results(self, name: str, file_id: str):
    return self.__dispatch_files(name, file_id, "OUT")

  def _get_path_from_name(self, name: str, file_type: str):
    return path.join(self.BASE_DIR, self.FOLDERS[file_type], name)

  def __dispatch_files(self, name: str, file_id: str, file_type: str):
    file_path = self._get_path_from_name(name, file_type)

    if path.exists(file_path):
      return self.FILE_READER.read_file(file_path)

    file = self.FILE_LOADER.load_file(file_id)
    self.__cache_file(file, file_type, name)
    return file

  def __cache_file(self, file, file_type, name):
    if file_type == "IN":
      self.FILE_SAVER.save_in_file(name, file)
    else:
      self.FILE_SAVER.save_out_file(name, file)

  def _add_base_dir(self, base_dir):
    if not path.exists(base_dir):
      raise Exception("Base dir doesn't exist")
    self.BASE_DIR = base_dir