from . import util
from .util.config import Config
from .util.logging import Log

# 'webdriver' relies on 'Config'
from . import webdriver
from .webdriver.driver import Driver

# 'elements' relies on 'Driver' and 'Config'
from . import elements
from .elements import *
from .elements.util.finder import Finder

# 'test' relies on everything (yeah)
from . import test
