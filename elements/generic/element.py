import sys

from selenium.webdriver.support import expected_conditions as EC

from ..util.finder import Finder
from . import Log
from . import wait_for


class Element (Finder):
    def __init__(self, *args, **kwargs):
        super(Element, self).__init__(*args, **kwargs)
        Log.info(self.hdr + '__init__() called.')

    @property
    def can_get(self):
        self.clog('can_get', prop=True)
        return wait_for(EC.presence_of_element_located(self.fid))

    @property
    def e(self):
        self.clog('e', prop=True)
        if self.can_get is False:
            return False
        else:
            return self.find()
