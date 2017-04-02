from abc import ABCMeta, abstractmethod

class Connector():
    __metaclass__ = ABCMeta

    @abstractmethod
    def setConnection(self, hostString, portString, dbString):
        pass

    @abstractmethod
    def closeConnection(self):
        pass

