import classes.log
import classes.config
#test
c = classes.config.Config()
classes.log.Log.setConfig(c.logFile)
mon = ConnectorMongo(c)
con = mon.setConnection()
coll = con['orders']
for ord in coll.find():
    print  ord
