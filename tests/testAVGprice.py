import test

class TestAVGprice(test.Test):

    def __init__(self, confObj):
        test.Test.__init__(self, confObj)

    def runTest(self):
        self.listAVGprice = {}

        for nameState, state in self.conf.stateOrderForIndex.items():
            for instr in self.conf.listInstrument:
                collectionPrice = self.conf.collectionObjects['repositoryRedis'].getCollection(nameState + 'Price' + str(instr))
                countPrice = 0
                if len(collectionPrice) > 0:
                    for price in collectionPrice:
                        countPrice += float(price)
                    self.listAVGprice[nameState + '_MiddlePrice_' + str(instr)] = round(countPrice / len(collectionPrice),5)
                else:
                    self.listAVGprice[nameState + '_MiddlePrice_' + str(instr)] = 0

        for key, value in self.listAVGprice.items():
            print '{0}:  {1}'.format(key, value)
            # print '/n'
