import utils.connector
import redis
#import classes.config

class ConnectorRedis(utils.connector.Connector):
    '''Class for connect to Redis'''

    def __init__(self, confObj):
        utils.connector.Connector.__init__(self, confObj)

    def setConnection(self):
        self.conn = redis.StrictRedis(host=self.conf.hostRedis,
                                      port=self.conf.portRedis,
                                      db=self.conf.dbRedis)
        return self.conn

    def closeConnection(self):
        pass

#test
#c = classes.config.Config()
#r = ConnectorRedis(c)
#con = r.setConnection()
#print con.get('test')
