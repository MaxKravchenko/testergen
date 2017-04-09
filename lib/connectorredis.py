import connector
import redis
#import classes.config

class ConnectorRedis(connector.Connector):
    '''Class for connect to Redis'''

    conn = None
    db = None
    isConnect = False


    def __init__(self, confObj):
        connector.Connector.__init__(self, confObj)

    def setConnection(self):
        try:
            self.conn = redis.Connection(host=self.conf.hostRedis,
                                      port=self.conf.portRedis,
                                      db=self.conf.dbRedis)
            self.conn.connect()
            self.conf.collectionObjects['log'].info('set connection is successful', self)
            self.isConnect = True
            self.db = redis.StrictRedis(host=self.conf.hostRedis,
                                      port=self.conf.portRedis,
                                      db=self.conf.dbRedis)
            return 'OK'
        except redis.ConnectionError, e:
            self.conf.collectionObjects['log'].warning(str(e), self)
            return e

    def closeConnection(self):
        if self.isConnect:
            self.conn.disconnect()
            self.conf.collectionObjects['log'].info('connection closed', self)
            self.isConnect = False
            return 'OK'
        else:
            self.conf.collectionObjects['log'].warning("connection not closed because connection doesn't exist", self)
            return 'NOT OK'

    def getDataRequest(self, key):
        if self.isConnect:
            collection = self.db.get(key)
            self.conf.collectionObjects['log'].info('data got from key ' + key, self)
            return collection
        else:
            self.conf.collectionObjects['log'].warning("data didn't get from collection because connection doesn't exist", self)
            return 'NOT OK'

    def execRequest(self, dataCollection, nameCollection):
        if self.isConnect:
            for key, value in dataCollection.items():
                self.db.set(key, value)
            self.conf.collectionObjects['log'].info('data insert ', self)
            return 'OK'
        else:
            self.conf.collectionObjects['log'].warning("data didn't insert because connection doesn't exist", self)
            return 'NOT OK'

    def countRowDB(self, nameCollection):
        pass

    def cleanDB(self, nameCollection):
        if self.isConnect:
            self.db.flushdb()
            self.conf.collectionObjects['log'].info('collection cleaned ', self)
            return 'OK'
        else:
            self.conf.collectionObjects['log'].warning("collection didn't clean because connection doesn't exist", self)
            return 'NOT OK'
