class WorkFlow():
    '''Class for organisation process'''
    conf = None

    def __init__(self, confObj):
        self.conf = confObj

    def execProcess(self):


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
