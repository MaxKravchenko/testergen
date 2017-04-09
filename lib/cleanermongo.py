import cleaner

class CleanerMongo(cleaner.Cleaner):

    def __init__(self, confObj):
        cleaner.Cleaner.__init__(self, confObj)

    def cleanDB(self):
        result = self.conf.collectionObjects['connectorMongo'].cleanDB(self.conf.nameCollectionMongo)
        return result
