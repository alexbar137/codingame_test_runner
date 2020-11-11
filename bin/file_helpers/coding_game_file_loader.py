from typing import List
import requests
from requests.exceptions import HTTPError

from bin.interfaces.file_loader_interface import FileLoaderInterface

class CodingGameFileLoader(FileLoaderInterface):
  def __init__(self):
    self.ROOT_ENDPOINT = "https://static.codingame.com/servlet/fileservlet?id="

  def load_file(self, file_id: str) -> List[str]:
    url = self.ROOT_ENDPOINT + file_id
    response = requests.get(url)
    if response.status_code != 200:
      raise HTTPError("Couldn't find the requested resource")
    return response.text.splitlines()
