from typing import List
import os

from bin.interfaces.file_saver_interface import FileSaverInterface

class GenericFileSaver(FileSaverInterface):

  def __init__(self, base_dir: str):
    super().__init__()
    self.BASE_DIR = base_dir
    self.IN_DIR = self.BASE_DIR + "/in"
    self.OUT_DIR = self.BASE_DIR + "/out"
    self.create_folders()

  def save_out_file(self, name: str, content: List[str]) -> None:
    pass

  def save_in_file(self, name: str, content: List[str]) -> None:
    pass

  def create_folders(self) -> None:
    if not os.path.exists(self.BASE_DIR):
      raise FileExistsError("'{0}' folder doesn't exist".format(self.BASE_DIR))

    if not os.path.exists(self.IN_DIR):
      os.mkdir(self.IN_DIR)
    if not os.path.exists(self.OUT_DIR):
      os.mkdir(self.OUT_DIR)