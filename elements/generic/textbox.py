from selenium.webdriver.support import expected_conditions as EC

from . import wait_for
from . import Element


class TextBox (Element):
    def __init__(self, *args, **kwargs):
        super(TextBox, self).__init__(*args, **kwargs)

    @property
    def can_read(self):
        self.clog('can_read', prop=True)
        return self.can_get

    def waitForValue(self, value):
        self.clog('waitForValue')
        return wait_for(EC.text_to_be_present_in_element(self.fid, value))

    @property
    def text(self):
        self.clog('text', prop=True)
        if self.can_read == False:
            return False
        else:
            return self.e.text
