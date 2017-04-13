import repository

class RepositoryRedis(repository.Repository):

    def __init__(self, confObj):
        repository.Repository.__init__(self, confObj)

    def setCollection(self, dataCollection, nameCollection):

        self.conf.collectionObjects['connectorRedis'].execRequest(dataCollection, nameCollection)

    def getCollection(self, key):

        dataCollection = self.conf.collectionObjects['connectorRedis'].getDataRequest(key)

        return dataCollection
