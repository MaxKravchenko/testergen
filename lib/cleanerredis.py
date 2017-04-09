import cleaner

class CleanerRedis(cleaner.Cleaner):

    def __init__(self, confObj):
        cleaner.Cleaner.__init__(self, confObj)

    def cleanDB(self):
        result = self.conf.collectionObjects['connectorRedis'].cleanDB(self.conf.nameCollectionRedis)
        return result
