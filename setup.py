# import cleaner
# import cleanermongo
# import cleanerredis
import lib.config as conf
import lib.connector as connector
import lib.connectormongo as connectormongo
import lib.connectorredis as connectorredis
# import generator
import lib.log as log
# import repository
# import repositoryredis
# import repositorymongo

class Setup():
    '''Setup objects'''

    def __init__(self):
        self.confObj = conf.Config()

    def createObjects(self):
        self.confObj.collectionObjects['log'] = log.Log(self.confObj)
        self.confObj.collectionObjects['connectorMongo'] = connectormongo.ConnectorMongo(self.confObj)
        # self.confObj.collectionObjects['connectorRedis'] = connectorredis.ConnectorRedis(self.confObj)

c = Setup()
c.createObjects()
c.confObj.collectionObjects['connectorMongo'].setConnection()
# for nameClass, linkObj in c.confObj.collectionObjects.items():
    # print 'Class {0} Object {1}'.format(nameClass, linkObj)
orders = c.confObj.collectionObjects['connectorMongo'].getDataRequest('orders')
print orders
