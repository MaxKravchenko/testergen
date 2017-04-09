import connector
from pymongo import MongoClient



class ConnectorMongo(connector.Connector):
    '''Class for connect to MongoDB'''

    conn = None
    db = None
    isConnect = False

    def __init__(self, confObj):
        connector.Connector.__init__(self, confObj)

    def setConnection(self):
        try:
            self.conn = MongoClient(self.conf.hostMongo, self.conf.portMongo)
            self.conf.collectionObjects['log'].info('set connection is successful', self)
            isConnect = True
        except pymongo.errors.ConnectionFailure, e:
            self.conf.collectionObjects['log'].warning(str(e), self)
            return 'NOT OK'

        self.db = self.conn[self.conf.dbMongo]
        return 'OK'

    def closeConnection(self):
        if self.isConnect:
            self.conn.Close()
            self.conf.collectionObjects['log'].info('connection closed', self)
            return 'OK'
        else:
            self.conf.collectionObjects['log'].warning("connection not closed because connection doesn't exist", self)
            return 'NOT OK'

    def getDataRequest(self, nameCollection):
        if self.isConnect:
            collection = self.db[nameCollection]
            self.conf.collectionObjects['log'].info('data got from collection ' + nameCollection, self)
            return collection
        else:
            self.conf.collectionObjects['log'].warning("data didn't get from collection because connection doesn't exist", self)
            return 'NOT OK'

    def execRequest(self, dataCollection, nameCollection):
        if self.isConnect:
            collection = self.db[nameCollection]
            collection.insert(dataCollection)
            self.conf.collectionObjects['log'].info('data insert into collection ' + nameCollection, self)
            return 'OK'
        else:
            self.conf.collectionObjects['log'].warning("data didn't insert into collection because connection doesn't exist", self)
            return 'NOT OK'

    def countRowBD(self, nameCollection):
        if self.isConnect:
            collection = self.db[nameCollection]
            self.conf.collectionObjects['log'].info('request (count row) exec ' + nameCollection, self)
            return collection.count()
        else:
            self.conf.collectionObjects['log'].warning("request didn't exec because connection doesn't exist", self)
            return 'NOT OK'

    def cleanBD(self, nameCollection):
        if self.isConnect:
            self.conn.drop_collection(nameCollection)
            self.conf.collectionObjects['log'].info('collection cleaned ' + nameCollection, self)
            return 'OK'
        else:
            self.conf.collectionObjects['log'].warning("collection didn't clean because connection doesn't exist", self)
            return 'NOT OK'
