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
    collectionVolumes = {'fill': 0,
                         'partialFill': 0,
                         'reject': 0,
                         'totalVolume': 0}
    collectionMiddlePrice = {}
    countRepeatInstrument = {}

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

    def genListOrders(self):

        # prepeared collection for indexes
        for nameState, state in self.conf.stateOrderForIndex.items():
            for instr in self.conf.listInstrument:
                self.countRepeatInstrument[nameState + 'count' + str(instr)] = 0
                self.collectionMiddlePrice[nameState + 'midPr' + str(instr)] = 0

        # generate orders and count indexes
        for i in range(1, self.conf.countOrders):
            orders = self.genOrder(i)
            self.collectionOrders.append(orders[0])
            self.collectionOrders.append(orders[1])

            #count volume for state
            for nameState, state in self.conf.stateOrderForIndex.items():
                if getattr(orders[1], 'stateOrder') == state:
                    self.collectionVolumes[nameState] += orders[1].volumeOrder
                    #prepare data for count middle price for instrument and state
                    for instr in self.conf.listInstrument:
                        if getattr(orders[1], 'instrument') == instr:
                            self.countRepeatInstrument[nameState + 'count' + str(instr)] += 1
                            self.collectionMiddlePrice[nameState + 'midPr' + str(instr)] += getattr(orders[1], 'pxOrder')


        #count total volume for all orders state
        self.collectionVolumes['totalVolume'] = self.collectionVolumes['fill'] + self.collectionVolumes['partialFill'] + self.collectionVolumes['reject']

        #count middle price for instrument and state
        for nameState, state in self.conf.stateOrderForIndex.items():
            for instr in self.conf.listInstrument:
                if self.countRepeatInstrument[nameState + 'count' + str(instr)] != 0:
                    self.collectionMiddlePrice[nameState + 'midPr' + str(instr)] = round(self.collectionMiddlePrice[nameState + 'midPr' + str(instr)] / self.countRepeatInstrument[nameState + 'count' + str(instr)], 5)
                else:
                    self.collectionMiddlePrice[nameState + 'midPr' + str(instr)] = 0



c = config.Config()
g = Generator(c)
g.genListOrders()

print g.collectionVolumes
print g.collectionMiddlePrice
print g.countRepeatInstrument
'''
list = []
for i in var:
    list.append('{' + \
                    'idOrder: ' + str(i.idOrder) + ', ' + \
                    'stateOrder: ' + str(i.stateOrder) + ', ' + \
                    'instrument: ' + "'" + i.instrument + "'" + ', ' + \
                    'dateOrder: ' + "'" + str(i.dateOrder) + "'" + ', ' + \
                    'pxOrder: ' + str(i.pxOrder) + ', ' + \
                    'volumeOrder: ' + str(i.volumeOrder) + ', ' + \
                    'pxfOrder: ' + str(i.pxfOrder) + ', ' + \
                    'volumefOrder: ' + str(i.volumefOrder) + ', ' + \
                    'directOrder: ' + "'" + str(i.directOrder) + "'" + \
                    '}\n')

proj_function.writeFile(list, 'testgen1.txt')
'''
