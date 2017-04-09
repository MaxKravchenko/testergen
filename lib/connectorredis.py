import connector
import redis
#import classes.config

class ConnectorRedis(connector.Connector):
    '''Class for connect to Redis'''

    conn = None
    isConnect = False

    def __init__(self, confObj):
        connector.Connector.__init__(self, confObj)

    def setConnection(self):
        self.conn = redis.StrictRedis(host=self.conf.hostRedis,
                                      port=self.conf.portRedis,
                                      db=self.conf.dbRedis)
        return self.conn

    def closeConnection(self):
        pass

    def getDataRequest(self):
        pass

    def execRequest(self):
        pass

    def cleanBD(self):
        pass


#test
#c = classes.config.Config()
#r = ConnectorRedis(c)
#con = r.setConnection()
#print con.get('test')
