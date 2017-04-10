# import cleaner
import lib.cleanermongo as cleanermongo
import lib.cleanerredis as cleanerredis
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
        self.confObj.collectionObjects['cleanerMongo'] = cleanermongo.CleanerMongo(self.confObj)
        self.confObj.collectionObjects['cleanerRedis'] = cleanerredis.CleanerRedis(self.confObj)

        for nameObj, linkObj in self.confObj.collectionObjects.items():
            if linkObj is not None:
                self.confObj.collectionObjects['log'].info('Object created successful', linkObj)
            else:
                self.conf.collectionObjects['log'].warning('Object' + nameObj + 'not created in class', self)
                print 'Object' + nameObj + 'not created'
                return 'NOT OK'
        return 'OK'

    def setConnections(self):
        connectors = [self.confObj.collectionObjects['connectorMongo'], self.confObj.collectionObjects['connectorRedis']]
        for connector in connectors:
            try:
                connector.setConnection()
            except Exception as e:
                print e
                return 'NOT OK'
        return 'OK'

    def cleanBases(self):
        cleaners = [self.confObj.collectionObjects['cleanerMongo'], self.confObj.collectionObjects['cleanerRedis']]
        for cleaner in cleaners:
            cleaner.cleanDB()
        return 'OK'

    def prepeareObjects(self):
        if self.createObjects() == 'OK':
            if self.setConnections() == 'OK':
                if self.cleanBases() == 'OK':
                    return 'OK'
                else: return 'NOT OK'
            else: return 'NOT OK'
        else: return 'NOT OK'
