from abc import *
import utils.connector

class Cleaner(metaclass = ABCMeta):

    @abstractmethod
    def CleanBD(self, connectorObj):
        pass