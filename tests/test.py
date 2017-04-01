from abc import *

from classes import config


class Test(metaclass = ABCMeta):

    @abstractmethod
    def runTest(self, configObj):
        pass