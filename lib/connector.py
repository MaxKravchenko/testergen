from abc import ABCMeta, abstractmethod

class Connector():
    __metaclass__ = ABCMeta

    def __init__(self, confObj):
        #link on configuration object
        self.conf = confObj

    @abstractmethod
    def setConnection(self):
        pass

    @abstractmethod
    def closeConnection(self):
        pass

    @abstractmethod
    def getDataRequest(self, nameCollection):
        pass

    @abstractmethod
    def execRequest(self, dataCollection, nameCollection):
        pass

    @abstractmethod
    def cleanBD(self):
        pass
