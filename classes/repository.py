from abc import *
import utils.connector
import classes.criteria
import classes.order

class Repository(metaclass = ABCMeta):

    @abstractmethod
    def setColecction(self, connectorObj, dataCollection, criteriaObj):
        pass

    @abstractmethod
    def getColecction(self, connectorObj, criteriaObj):
        return dataCollection