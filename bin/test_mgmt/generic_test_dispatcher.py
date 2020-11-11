from bin.interfaces.test_dispatcher_interface import TestDispatcherInterface

class GenericTestDispatcher(TestDispatcherInterface):
  def __init__(self, options):
    super(GenericTestDispatcher, self).__init__(options)

  def get_puzzle(self, name: str, file_id: str):
    pass

  def get_expected_results(self, name: str, file_id: str):
    pass