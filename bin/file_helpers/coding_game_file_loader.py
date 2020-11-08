from typing import List
import requests

from bin.interfaces.file_loader_interface import FileLoaderInterface

class CodingGameFileLoader(FileLoaderInterface):
  def __init__(self):
    self.ROOT_ENDPOINT = "https://static.codingame.com/servlet/fileservlet?id="

  def load_file(self, file_id: str) -> List[str]:
    url = self.ROOT_ENDPOINT + file_id
    return requests.get(url).text.splitlines()

