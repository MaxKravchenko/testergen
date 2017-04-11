import repository

class RepositoryMongo(repository.Repository):

    def __init__(self, confObj):
        repository.Repository.__init__(self, confObj)

    def setCollection(self, dataCollection):

        listOrders = []

        for order in dataCollection:
            itemList = {"idOrder": order.idOrder,
                        "stateOrder": order.stateOrder,
                        "instrument": order.instrument,
                        "dateOrder": order.dateOrder,
                        "pxOrder": order.pxOrder,
                        "volumeOrder": order.volumeOrder,
                        "pxfOrder": order.pxfOrder,
                        "volumefOrder": order.volumefOrder,
                        "directOrder": order.directOrder}

            listOrders.append(itemList)

        self.conf.collectionObjects['connectorMongo'].execRequest(listOrders, self.conf.nameCollectionMongo)

    def getCollection(self):
        return dataCollection
