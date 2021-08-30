import logging

class LoggGeneration:
    @staticmethod
    def logGenerate():
        Log_Format = '%(asctime)s %(message)s'
        logging.basicConfig(level=logging.INFO,filename='C:\\Users\\sukal\\PycharmProjects\\Test\\Logs\\Automation.log',format=Log_Format,force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

