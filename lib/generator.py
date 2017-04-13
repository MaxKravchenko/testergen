import order
import config
import random
import datetime
import math
import copy
import proj_function

class Generator():
    '''Generation data for order'''
    collectionOrders = []

    def __init__(self, confObj):
        #link on configuration object
        self.conf = confObj

    # generation ID
    def genID(self, lastIterable):
        nextID = lastIterable * 21 + math.sin(lastIterable) * 20
        return int(nextID)

    # generation Direct
    def genStateNewOrder(self):
        return self.conf.stateOrder['new']

    # generation Direct
    def genDirect(self):
        return random.choice(self.conf.direct)

    # generation volume
    def genVolume(self):
        lowVolume = self.conf.volumeOrders[0] / 1000
        highVolume = self.conf.volumeOrders[1] / 1000
        return random.randint(lowVolume, highVolume) * 1000

    # generation random instrument from a tuple
    def genInstrument(self):
        return random.choice(self.conf.listInstrument)

    # generation px
    def genPx(self, instrument):
        etalonPx = self.conf.listInstrumentPrice[instrument]
        isPlus = random.randint(0, 1)
        offset = (etalonPx * (random.random() * self.conf.deltaPxOrder))

        if isPlus:
            px = etalonPx + offset
        else:
            px = etalonPx - offset
        return round(px, 5)

    # generation date
    def genDate(self):
        # split date
        buildFromD = datetime.date(self.conf.fromYear, self.conf.fromMonth, self.conf.fromDate)
        buildToD = datetime.date(self.conf.toYear, self.conf.toMonth, self.conf.toDate)

        # generation date
        if buildToD > buildFromD:
            d1 = buildFromD.day
            d2 = buildToD.day
            daysInPeriod = d2 - d1
            randOfssetDay = random.randint(0, daysInPeriod - 1)
            randOfssetMinutes = random.randint(0, 59)
            randOfssetHour = random.randint(0, 23)
            goalDate = datetime.datetime(self.conf.fromYear,
                                         self.conf.fromMonth,
                                         self.conf.fromDate + randOfssetDay,
                                         randOfssetHour,
                                         randOfssetMinutes)
            return goalDate
        # wrong input date
        else:
            print 'Start date {0} > End date {1}'.format(buildToD, buildFromD)
            return 1

    # generation new date
    def modifyDate(self, dateNewOrder):
        newDate = dateNewOrder.replace(second=random.randint(0, 59))
        return newDate

    # generation state
    def genState(self):
        countFill = self.conf.stateRange['1']
        countPartialFill = self.conf.stateRange['1'] + self.conf.stateRange['2']
        randNum = random.random()
        if randNum < countFill:
            goalState = self.conf.stateOrder['fill']
        elif randNum >= countFill and randNum <= countPartialFill:
            goalState = self.conf.stateOrder['partialFill']
        elif randNum > countPartialFill:
            goalState = self.conf.stateOrder['reject']
        return goalState

    # generation PxF
    def genPxF(self, stateOrder, pxOrder, directOrder):
        if directOrder == 'buy' and stateOrder != self.conf.stateOrder['reject']:
            goalPxF = pxOrder + self.conf.deltaPxOrder
        elif directOrder == 'sell' and stateOrder != self.conf.stateOrder['reject']:
            goalPxF = pxOrder - self.conf.deltaPxOrder
        elif stateOrder == self.conf.stateOrder['reject']:
            goalPxF = 0
        return round(goalPxF, 5)

    # generation volumeF
    def genVolumeF(self, stateOrder, volumeOrder):

        if stateOrder == self.conf.stateOrder['reject']:
            VolumeF = 0
        elif stateOrder == self.conf.stateOrder['fill']:
            VolumeF = volumeOrder
        elif stateOrder == self.conf.stateOrder['partialFill']:
            VolumeF = volumeOrder * self.conf.deltaVolumeForPartialFill
        return round(VolumeF)

    # generation order
    def genOrder(self, lastIterable):
        self.newOrder = order.Order()
        self.processedOrder = order.Order()

        #generation new order
        self.newOrder.idOrder = self.genID(lastIterable + 1)
        for field, method in self.conf.mappingFieldMethod.items():
            if hasattr(self, method):
                setMethod = getattr(self, method)
                setattr(self.newOrder, field, setMethod())
        self.newOrder.pxOrder = self.genPx(self.newOrder.instrument)

        #generation processed order
        self.processedOrder = copy.copy(self.newOrder)
        self.processedOrder.stateOrder = self.genState()
        self.processedOrder.dateOrder = self.modifyDate(self.newOrder.dateOrder)
        self.processedOrder.pxfOrder = self.genPxF(self.processedOrder.stateOrder,
                                                    self.newOrder.pxOrder,
                                                    self.newOrder.directOrder)
        self.processedOrder.volumefOrder = self.genVolumeF(self.processedOrder.stateOrder, self.newOrder.volumeOrder)

        #add to list
        orders = [self.newOrder, self.processedOrder]
        return orders

    def createStructuresForRedis(self):
        # prepeared collection for indexes
        for nameState, state in self.conf.stateOrderForIndex.items():
            setattr(self, nameState, {})
            for instr in self.conf.listInstrument:
                setattr(self, nameState + 'Price' + str(instr), {})
                # print type(getattr(self, nameState + 'Price' + str(instr)))


    def genListOrders(self):
        # prepeared collection for indexes
        self.createStructuresForRedis()

        # generate orders and count indexes
        for i in range(1, self.conf.countOrders):
            orders = self.genOrder(i)
            self.collectionOrders.append(orders[0])
            self.collectionOrders.append(orders[1])
            #generation indexes for redis
            self.genIndexesForRedis(orders[1])

        #save to MongoDB
        self.conf.collectionObjects['repositoryMongo'].setCollection(self.collectionOrders)

        #save to Redis
        # self.saveIndexesToRedis()

    def genIndexesForRedis(self, order):
        #volume for state
        for nameState, state in self.conf.stateOrderForIndex.items():
            if getattr(order, 'stateOrder') == state:
                setattr(self, nameState, {getattr(order, 'idOrder'): getattr(order, 'volumeOrder')})
                #save to Redis
                self.conf.collectionObjects['repositoryRedis'].setCollection(getattr(self, nameState), nameState)
                #middle price for instrument and state
                for instr in self.conf.listInstrument:
                    if getattr(order, 'instrument') == instr:
                        setattr(self, nameState + 'Price' + str(instr), {getattr(order, 'idOrder'): getattr(order, 'pxOrder')})
                        #save to Redis
                        self.conf.collectionObjects['repositoryRedis'].setCollection(getattr(self, nameState + 'Price' + str(instr)), nameState + 'Price' + str(instr))
