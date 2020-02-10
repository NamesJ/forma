from selenium.webdriver.support import expected_conditions as EC

from . import TextBox
from . import ClickBox
from . import wait_for


class TextField (TextBox, ClickBox):
    def __init__(self, *args, **kwargs):
        super(TextField, self).__init__(*args, **kwargs)

    @property
    def can_write(self):
        self.clog('can_write', prop=True)
        return wait_for(EC.presence_of_element_located(self.fid))

    @property
    def text(self):
        self.clog('text', prop=True)
        super(TextField, self).text

    # NOTE: TextBox class defined property 'text' for read operation
    @text.setter
    def text(self, text):
        self.clog('text.setter', prop=True)
        if self.can_write == False:
            return False
        else:
            self.e.clear()
            self.e.send_keys(text)
            return True
