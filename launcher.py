import setup

setupObj = setup.Setup()
resultSetup = setupObj.prepeareObjects()
if resultSetup == 'NOT OK':
    print 'Process setup was wrong'
