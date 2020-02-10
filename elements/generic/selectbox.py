from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from . import wait_for
from . import Element

class SelectBox (Element):
    def __init__(self, *args, **kwargs):
        super(SelectBox, self).__init__(*args, **kwargs)

    @property
    def can_select(self):
        self.clog('can_select', prop=True)
        return self.can_get

    @property
    def selecter(self):
        self.clog('selecter', prop=True)
        if self.can_select == False:
            return False
        else:
            return Select(self.e)

    def select_by_value(self, value):
        self.clog('select_by_value')
        s = self.selecter
        if s == False:
            return False
        else:
            s.select_by_value(value)
            return True

    def select_by_index(self, index):
        self.clog('select_by_index')
        s = self.selecter
        if s == False:
            return False
        else:
            s.select_by_index(index)
            return True

    def select_by_visible_text(self, text):
        self.clog('select_by_visible_text')
        s = self.selecter
        if s is False:
            return False
        else:
            s.select_by_visible_text(text)
            return True
