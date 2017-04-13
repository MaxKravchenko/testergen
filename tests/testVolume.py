import test

class TestVolume(test.Test):

    def __init__(self, confObj):
        test.Test.__init__(self, confObj)

    def runTest(self):
        self.listVolumes = {}

        for nameState, state in self.conf.stateOrderForIndex.items():
            collectionVolumes = self.conf.collectionObjects['repositoryRedis'].getCollection(nameState)
            countVolume = 0
            for volume in collectionVolumes:
                countVolume += int(volume)
            self.listVolumes[nameState] = countVolume

        self.listVolumes['Total volume'] = 0
        for nameState, state in self.conf.stateOrderForIndex.items():
            # totalVolume += self.listVolumes[nameState]
            self.listVolumes['Total volume'] += self.listVolumes[nameState]

        print self.listVolumes
