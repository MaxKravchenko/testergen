import lib.config as conf
import lib.connectormongo
import lib.log

#test
c = conf.Config()
l = log.Log(c.logFile)
mongo = connectormongo.ConnectorMongo(c)
connect = mongo.setConnection()
collection = connect['orders']
for ord in collection.find():
    print  ord
