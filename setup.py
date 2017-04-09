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
        self.confObj.collectionObjects['connectorRedis'] = connectorredis.ConnectorRedis(self.confObj)

c = Setup()
c.createObjects()
c.confObj.collectionObjects['connectorRedis'].setConnection()
c.confObj.collectionObjects['connectorMongo'].setConnection()


# print c.confObj.collectionObjects['connectorRedis'].getDataRequest('test')
# post = {'key1': 10, 'key2': 10, 'key3': 10}
# c.confObj.collectionObjects['connectorRedis'].execRequest(post, None)
# c.confObj.collectionObjects['connectorRedis'].cleanDB(None)
# c.confObj.collectionObjects['connectorRedis'].closeConnection()

# c.confObj.collectionObjects['connectorMongo'].setConnection()
# for nameClass, linkObj in c.confObj.collectionObjects.items():
    # print 'Class {0} Object {1}'.format(nameClass, linkObj)
# orders = c.confObj.collectionAObjects['connectorMongo'].getDataRequest('orders')
# for data in orders.find():
    # print data
# print c.confObj.collectionObjects['connectorMongo'].countRowDB('orders')
# post = {'key1': 1, 'key2': 'str', 'key3': 5}
# c.confObj.collectionObjects['connectorMongo'].execRequest(post, 'orders')
# c.confObj.collectionObjects['connectorMongo'].cleanDB('orders')
# c.confObj.collectionObjects['connectorMongo'].closeConnection()
