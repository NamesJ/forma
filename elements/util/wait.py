from . import Driver
from . import Log

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def clog(self, func, prop=False):
    sProp = 'property ' if prop else ''
    message = '%s() %swas called.' % (func, sProp)
    Log.debug(message)

def wait_for(event, seconds=10):
    Log.debug('wait_for() called: event=%s, seconds=%d' % (event, seconds))
    driver = Driver()
    wait = WebDriverWait(driver, seconds)
    try:
        wait.until(event)
    except TimeoutException:
        return False
    else:
        return True
