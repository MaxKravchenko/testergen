class Order:
    '''Entity order'''

    # setters
    def setIdOrder(self, idOrder):
        if idOrder > 0:
            self.idOrder = idOrder
        else:
            self.idOrder = 0

    def setStateOrder(self, stateOrder):
        self.stateOrder = stateOrder

    def setInstrument(self, instrument):
        self.instrument = instrument

    def setDateOrder(self, dateOrder):
        self.dateOrder = dateOrder

    def setPxOrder(self, pxOrder):
        self.pxOrder = pxOrder

    def setVolumeOrder(self, volumeOrder):
        self.volumeOrder = volumeOrder

    def setPxfOrder(self, pxfOrder):
        self.pxfOrder = pxfOrder

    def setVolumefOrder(self, volumefOrder):
        self.volumefOrder = volumefOrder

    def setDirectOrder(self, directOrder):
        self.directOrder = directOrder

    #getters
    def getIdOrder(self):
        return self.idOrder

    def getStateOrder(self):
        return self.stateOrder

    def getInstrument(self):
        return self.instrument

    def getDateOrder(self):
        return self.dateOrder

    def getPxOrder(self):
        return self.pxOrder

    def getVolumeOrder(self):
        return self.volumeOrder

    def getPxfOrder(self):
        return self.pxfOrder

    def getVolumefOrder(self):
        return self.volumefOrder

    def getDirectOrder(self):
        return self.directOrder