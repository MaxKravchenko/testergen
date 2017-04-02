import utils.connector
import redis

class ConnectorRedis(utils.connector.Connector):
    '''Class for connect to Redis'''

    def setConnection(self, hostString, portString, dbString):
        self.conn = redis.StrictRedis(host=hostString, port=portString, db=dbString)
        return self.conn

    def closeConnection(self):
        pass

#r = ConnectorRedis()
#con = r.setConnection('localhost', 6379, '0')
#print con.get('test')
