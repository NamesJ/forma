import inspect
import logging
import os
from datetime import datetime
from datetime import timedelta

from .config import Config


class Log (object):
    initialized = False
    named_levels = {
        'DEBUG'    : logging.DEBUG,
        'INFO'     : logging.INFO,
        'WARNING'  : logging.WARNING,
        'ERROR'    : logging.ERROR,
        'CRITICAL' : logging.CRITICAL
    }
    tsfmt = None

    @staticmethod
    def ensureInitialized():
        if Log.initialized:
            return
        else:
            Log.initialize()

    @staticmethod
    def initialize(loglevel=None, logfile=None):
        Log.initialized = True

        # Set logging variables from configured settings (None if not exist)
        level = Config.get('loglevel')
        file = Config.get('logfile')
        timestamp_format = Config.get('timestamp_format')

        # If logging settings passed explicitly, override configuration.
        if loglevel is not None:
            level = loglevel
        if logfile is not None:
            file = logfile
        if timestamp_format is not None:
            Log.ts_format = timestamp_format

        if file is not None:
            if os.path.exists(file):
                os.remove(file)

        if level is not None and file is not None:
            logging.basicConfig(level=level, filename=file)
            return

        if level is not None:
            logging.basicConfig(level=level)
            return

        if file is not None:
            logging.basicConfig(filename=file)
            return
        # If this point is reached, then default settings are used.

    @staticmethod
    def getTimestamp():
        return str(datetime.today().strftime('%Y.%m.%d.%H.%M.%S'))

    @staticmethod
    def formatMessage(message):
        return Log.getTimestamp() + '\n' + message

    @staticmethod
    def debug(message):
        logging.debug(Log.formatMessage(message))


    @staticmethod
    def info(message):
        logging.info(Log.formatMessage(message))


    @staticmethod
    def warning(message):
        logging.warning(Log.formatMessage(message))


    @staticmethod
    def error(message):
        logging.error(Log.formatMessage(message))


    @staticmethod
    def critical(message):
        logging.critical(Log.formatMessage(message))



# Initialize Log on import
Log.ensureInitialized()
