from bin.interfaces.file_reader_interface import FileReaderInterface
from typing import List, Dict
import json
from pathlib import Path

class JsonTestCaseReader(FileReaderInterface):
  def read_file(self, path: str) -> List[Dict]:
    if Path(path).suffix != ".json":
      raise Exception("Please save test cases into a json file")

    with open(path) as json_file:
      file_content = json.load(json_file)
      return self.__update_dict_key_names(file_content["currentQuestion"]["question"]["testCases"])

  @staticmethod
  def __update_dict_key_names(content):
    for test_case in content:
      test_case.pop("index")
      test_case["puzzle_id"] = test_case.pop("inputBinaryId")
      test_case["expected_results_id"] = test_case.pop("outputBinaryId")

    return content


