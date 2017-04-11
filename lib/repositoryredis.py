import repository

class RepositoryRedis(repository.Repository):

    def __init__(self, confObj):
        repository.Repository.__init__(self, confObj)

    def setCollection(self, dataCollection):
        pass

    def getCollection(self):
        return dataCollection
