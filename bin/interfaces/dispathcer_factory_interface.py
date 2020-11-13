from abc import ABC, abstractmethod
from bin.interfaces.test_dispatcher_interface import TestDispatcherInterface

class DispatcherFactoryInterface(ABC):
  def __init__(self):
    super(DispatcherFactoryInterface, self).__init__()

  @abstractmethod
  def get_dispatcher(self) -> TestDispatcherInterface:
    pass