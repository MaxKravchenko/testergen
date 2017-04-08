import logging

class Log():
    '''Class for logging'''

    obj = None
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj

    def __init__(self, nameLogFile):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filename=nameLogFile,
            filemode='w'
        )

    def debug(message, linkObj):
        logging.debug(message + type(linkObj))

    def info(message, linkObj):
        logging.info(message + type(linkObj))

    def warning(message, linkObj):
        logging.warning(message + type(linkObj))
