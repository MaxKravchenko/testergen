import utils.connector
import pymongo

class ConnectorMongo(utils.connector.Connector):
    '''Class for connect to MongoDB'''
    def setConnection(self, hostString, portString, dbString):
        self.conn = pymongo.Connection(hostString, portString)
        self.db = self.conn[dbString]
        return self.db

    def closeConnection(self):
        pass

#mon = ConnectorMongo()
#con = mon.setConnection('localhost', 27017, 'test')
#coll = con['orders']
#for ord in coll.find():
#    print  ord
