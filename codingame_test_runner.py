from bin.test_mgmt.generic_settings_reader_factory import GenericSettingsReaderFactory
from bin.test_mgmt.generic_test_dispatcher_factory import GenericTestDispatcherFactory

class CodingameTestRunner:
  def __init__(self):
    self.settings_reader_factory = GenericSettingsReaderFactory()
    self.settings_reader = self.settings_reader_factory.get_settings_reader()
    self.BASE_DIR = self.settings_reader.get_base_dir()
    self.TEST_CASES = self.settings_reader.get_test_cases()

    self.dispatcher_factory = GenericTestDispatcherFactory(self.BASE_DIR)
    self.dispatcher = self.dispatcher_factory.get_dispatcher()

  def get_puzzle(self, test_case_index):
    test_case = self.TEST_CASES[int(test_case_index)]
    return self.dispatcher.get_puzzle(test_case["label"], test_case["puzzle_id"])

  def get_expected_results(self, test_case_index):
    test_case = self.TEST_CASES[int(test_case_index)]
    return self.dispatcher.get_expected_results(test_case["label"], test_case["expected_results_id"])

  def get_test_cases(self):
    test_cases = []
    for i in range(len(self.TEST_CASES)):
      puzzle = self.get_puzzle(i)
      expected_results = self.get_expected_results(i)
      test_cases.append({
        "puzzle": puzzle,
        "expected_results": expected_results,
        "label": self.TEST_CASES[i]["label"]
      })

    return test_cases
