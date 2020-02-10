from selenium import webdriver
import os
import sys

from . import Config
from . import Log


# Singleton webdriver
class Driver (object):
    instance = None

    def __new__(self):
        if Driver.instance is None:
            Driver._set_instance()
        else:
            Driver.instance.open()

        return Driver.instance

    @staticmethod
    def _set_instance():
        browser = Config.get('browser')
        Log.debug('Driver: browser=%s' % (browser))
        if browser == 'Chrome':
            Driver.instance = Singleton_ChromeWebdriver()
        else:
            Log.error('Currently, Chrome is the only supported browser.')
            sys.exit(1)


class Singleton_Counter (object):
    def __init__(self):
        self.numOpen = 0

    def open(self):
        self.numOpen += 1

    def release(self):
        self.numOpen -= 1

    def allReleased(self):
        if self.numOpen < 1:
            return True
        else:
            return False



class Singleton_ChromeWebdriver (webdriver.Chrome):
    def __init__(self):
        webdriver_path = Config.get('webdriver')
        super(Singleton_ChromeWebdriver, self).__init__(webdriver_path)
        self.counter = Singleton_Counter()
        self.counter.open()

    def open(self):
        self.counter.open()

    def release(self):
        self.count.release()                                                    # Call 'release()' for Singleton to decrement self.numOpen
        if self.counter.allReleased():                                          # Check if all references have been released
            self.close()                                                        # If yes, then close webdriver

    def allReleased(self):
        self.counter.allReleased()
