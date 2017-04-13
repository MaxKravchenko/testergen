from abc import ABCMeta, abstractmethod

class Test():
    __metaclass__ = ABCMeta

    conf = None

    def __init__(self, confObj):
        #link on configuration object
        self.conf = confObj

    @abstractmethod
    def runTest(self):
        pass
