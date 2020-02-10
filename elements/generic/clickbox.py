from selenium.webdriver.support import expected_conditions as EC

from . import Element
from . import Log
from . import wait_for


class ClickBox (Element):
    def __init__(self, *args, **kwargs):
        super(ClickBox, self).__init__(*args, **kwargs)

    @property
    def can_click(self):
        self.clog('can_click', prop=True)
        return wait_for(EC.element_to_be_clickable(self.fid))

    def click(self):
        self.clog('click')
        if self.can_click == False:
            return False
        else:
            self.e.click()
            return True
