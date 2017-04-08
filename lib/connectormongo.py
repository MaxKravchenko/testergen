import connector as conn
import pymongo



class ConnectorMongo(conn.Connector):
    '''Class for connect to MongoDB'''
    def __init__(self, confObj):
        conn.Connector.__init__(self, confObj)

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
