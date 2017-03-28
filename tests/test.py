from abc import *
import config.config

class Test(metaclass = ABCMeta):

    @abstractmethod
    def runTest(self, configObj):
        pass