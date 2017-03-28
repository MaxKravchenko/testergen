from abc import *

class Connector(metaclass = ABCMeta):

    @abstractmethod
    def Connect(self, connectionString):
        return connector

    @abstractmethod
    def CloseConnection(self, connectionString):
        pass