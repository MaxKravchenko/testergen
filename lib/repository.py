from abc import ABCMeta, abstractmethod

class Repository():
    __metaclass__ = ABCMeta

    conf = None

    def __init__(self, confObj):
        #link on configuration object
        self.conf = confObj

    @abstractmethod
    def setCollection(self, dataCollection):
        pass

    @abstractmethod
    def getCollection(self):
        return dataCollection
