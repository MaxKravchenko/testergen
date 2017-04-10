class Config(object):
    '''Contain parameters for program '''

    obj = None
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj

    def __init__(self):
        #list parameters
        self.countOrders = 1001
        self.stateOrder = {'new': 0,
                           'fill': 1,
                           'partial_fill': 2,
                           'reject': 8}
        self.stateOrderForTest = ('fill',
                                  'partial_fill',
                                  'reject')
        self.stateRange = {'1': 0.6,
                           '2': 0.1,
                           '8': 0.3}
        self.listInstrument = ('EUR/USD', 'AUD/CAD', 'CHF/GBP', 'CHF/USD')
        self.listInstrumentPrice = {'EUR/USD': 1.05942,
                                    'AUD/CAD': 0.99862,
                                    'CHF/GBP': 0.79363,
                                    'CHF/USD': 0.99427}
        self.deltaPxOrder = 0.05
        self.deltaVolumeForPartialFill = 0.5
        self.volumeOrders = (1000, 100000)
        self.direct = ('buy', 'sell')

        #interval period
        self.fromYear = 2017
        self.fromMonth = 02
        self.fromDate = 24
        self.toYear = 2017
        self.toMonth = 02
        self.toDate = 26

        #for sql insert
        self.templateForSqlQueryStart = 'INSERT INTO orders (Id,State,Instrument,Date,Px,Volume,PxF,VolumeF,Direct) VALUES ('
        self.templateForSqlQueryEnd = ');\n'
        self.nameFileForSqlQuery = 'orders.sql'

        #for mongodb
        self.templateForMongoQueryStart = 'db.orders.insert({'
        self.templateForMongoQueryEnd = '})\n'
        self.nameFileForMongoQuery = 'orders.json'

        #for validate structure orders
        self.listField = ('idOrder',
                          'stateOrder',
                          'instrument',
                          'dateOrder',
                          'pxOrder',
                          'volumeOrder',
                          'pxfOrder',
                          'volumefOrder',
                          'directOrder')
        #report files
        self.fileNameTest1 = 'result_test1.txt'
        self.fileNameTest2 = 'result_test2.txt'

        #connection options for mongodb
        self.hostMongo = 'localhost'
        self.portMongo = 27017
        self.dbMongo = 'test'
        self.nameCollectionMongo = 'orders'

        #connection options for redis
        self.hostRedis = 'localhost'
        self.portRedis = 6379
        self.dbRedis = '0'
        self.nameCollectionRedis = None

        #File for log
        self.logFile = 'testergen.log'

        #collection objects for application
        self.collectionObjects = {'log': None,
                                    'connectorMongo': None,
                                     'connectorRedis': None,
                                     'cleanerMongo': None,
                                     'cleanerRedis': None}
        #key - orders field, value - function
        self.mappingFieldMethod = {'stateOrder': 'genStateNewOrder',
                                     'instrument': 'genInstrument',
                                     'dateOrder': 'genDate',
                                     'volumeOrder': 'genVolume',
                                     'directOrder': 'genDirect'}
