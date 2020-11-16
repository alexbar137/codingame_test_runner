from bin.interfaces.file_reader_interface import FileReaderInterface
from typing import List, Dict
import json
from pathlib import Path

class JsonTestCaseReader(FileReaderInterface):
  def read_file(self, path: str) -> List[Dict]:
    if Path(path).suffix != ".json":
      raise Exception("Please save test cases into a json file")

    with open(path, encoding="utf8") as json_file:
      file_content = json.load(json_file)
      return self.__update_dict_key_names(file_content["currentQuestion"]["question"]["testCases"])

  @staticmethod
  def __update_dict_key_names(content):
    for test_case in content:
      test_case.pop("index")
      temp_label = test_case.pop("label")
      test_case["label"] = "".join(x for x in temp_label if x.isalnum())
      test_case["puzzle_id"] = test_case.pop("inputBinaryId")
      test_case["expected_results_id"] = test_case.pop("outputBinaryId")

    return content


