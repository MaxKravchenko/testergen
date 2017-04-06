import utils.connector
import pymongo
import classes.log
import classes.config

class ConnectorMongo(utils.connector.Connector):
    '''Class for connect to MongoDB'''

    def __init__(self, confObj):
        utils.connector.Connector.__init__(self, confObj)

    def setConnection(self):
        try:
            self.conn = pymongo.Connection(self.conf.hostMongo, self.conf.portMongo)
            classes.log.Log.info('set connection is successful')
        except pymongo.errors.ConnectionFailure, e:
            classes.log.Log.info(e)
            return 1

        self.db = self.conn[self.conf.dbMongo]

        return self.db

    def closeConnection(self):
        pass

#test
c = classes.config.Config()
classes.log.Log.setConfig(c.logFile)
mon = ConnectorMongo(c)
con = mon.setConnection()
coll = con['orders']
for ord in coll.find():
    print  ord
