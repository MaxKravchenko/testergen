class WorkFlow():
    '''Class for process'''
    conf = None

    def __init__(self, confObj):
        self.conf = confObj

    def execProcess(self):
        self.conf.collectionObjects['generator'].genListOrders()
        self.conf.collectionObjects['testVolume'].runTest()
        self.conf.collectionObjects['testAVGprice'].runTest()
