import logging

class Log():
    '''Class for logging'''

    obj = None
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj

    def __init__(self, confObj):
        self.conf = confObj

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filename=confObj.logFile,
            filemode='w'
        )

    def debug(self, message, linkObj):
        logging.debug(message + '  ' + str(type(linkObj)))

    def info(self, message, linkObj):
        logging.info(message + '  ' + str(type(linkObj)))

    def warning(self, message, linkObj):
        logging.warning(message + '  ' + str(type(linkObj)))
