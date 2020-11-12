from bin.interfaces.test_dispatcher_interface import TestDispatcherInterface
from os import path

class GenericTestDispatcher(TestDispatcherInterface):
  FOLDERS = {
    "OUT": "in",
    "IN": "out"
  }

  def __init__(self, options):
    super(GenericTestDispatcher, self).__init__(options)

  def get_puzzle(self, name: str, file_id: str):
    return self.__dispatch_files(name, file_id, "IN")

  def get_expected_results(self, name: str, file_id: str):
    return self.__dispatch_files(name, file_id, "OUT")

  def _get_path_from_name(self, name: str, file_type: str):
    return path.join(self.BASE_DIR, self.FOLDERS[file_type], name)

  def __dispatch_files(self, name: str, file_id: str, file_type: str):
    file_path = self._get_path_from_name(name, file_type)

    if self.FILE_READER.file_exists(file_path):
      return self.FILE_READER.read_file(file_path)

    file = self.FILE_LOADER.load_file(file_id)
    self.__cache_file(file, file_type, name)
    return file

  def __cache_file(self, file, file_type, name):
    if file_type == "IN":
      self.FILE_SAVER.save_in_file(name, file)
    else:
      self.FILE_SAVER.save_out_file(name, file)