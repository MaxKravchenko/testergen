from abc import ABCMeta, abstractmethod

class Cleaner():
    __metaclass__ = ABCMeta

    conf = None

    def __init__(self, confObj):
        #link on configuration object
        self.conf = confObj

    @abstractmethod
    def cleanDB(self):
        pass
