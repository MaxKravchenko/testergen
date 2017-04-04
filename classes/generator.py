import classes.order
import classes.conf
import random
import datetime
import math
import classes.proj_function


class Generator():
    '''Generation data for order'''

    def __init__(self, confObj):
        #link on configuration object
        self.conf = confObj

    # generation ID
    def genID(self, lastIterable):
        nextID = lastIterable * 21 + math.sin(lastIterable) * 20
        return int(nextID)

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
            goalState = self.conf.stateOrder['partial_fill']
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
        elif stateOrder == self.conf.stateOrder['partial_fill']:
            VolumeF = volumeOrder * self.conf.deltaVolumeForPartialFill
        return round(VolumeF)

    # generation order
    def genOrders(self, lastIterable):
        # gen data for new orders
        idOrder = self.genID(lastIterable + 1)
        stateNewOrder = self.conf.stateOrder['new']
        instrument = self.genInstrument()
        dateNewOrder = self.genDate()
        pxOrder = self.genPx(instrument)
        volumeOrder = self.genVolume()
        directOrder = self.genDirect()
        # gen data for processed orders
        stateProcessedOrder = self.genState()
        pxfOrder = self.genPxF(stateProcessedOrder, pxOrder, directOrder)
        volumefOrder = self.genVolumeF(stateProcessedOrder, volumeOrder)
        dateProcessedOrder = self.modifyDate(dateNewOrder)

        dictOrders = {'idOrder': idOrder,
                      'stateNewOrder': stateNewOrder,
                      'instrument': instrument,
                      'dateNewOrder': dateNewOrder,
                      'pxOrder': pxOrder,
                      'volumeOrder': volumeOrder,
                      'directOrder': directOrder,
                      'stateProcessedOrder': stateProcessedOrder,
                      'pxfOrder': pxfOrder,
                      'volumefOrder': volumefOrder,
                      'dateProcessedOrder': dateProcessedOrder}

        return dictOrders