import logging

class Log():
    '''Class for logging'''

    @staticmethod
    def setConfig(nameLogFile):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filename=nameLogFile,
            filemode='w'
        )

    @staticmethod
    def debug(message):
        logging.debug(message)

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

