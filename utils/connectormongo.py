import utils.connector
import pymongo
#import classes.config

class ConnectorMongo(utils.connector.Connector):
    '''Class for connect to MongoDB'''

    def __init__(self, confObj):
        utils.connector.Connector.__init__(self, confObj)

    def setConnection(self):
        self.conn = pymongo.Connection(self.conf.hostMongo,
                                       self.conf.portMongo)
        self.db = self.conn[self.conf.dbMongo]
        return self.db

    def closeConnection(self):
        pass

#test
# c = classes.config.Config()
#mon = ConnectorMongo(c)
#con = mon.setConnection()
#coll = con['orders']
#for ord in coll.find():
#    print  ord
