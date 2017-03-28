from abc import *

class Report(metaclass = ABCMeta):

    @abstractmethod
    def genReport(self, filename):
        pass
