from . import SelectBox
from . import ClickBox
from . import Log


class SelectField (SelectBox, ClickBox):
    def __init__(self, *args, **kwargs):
        super(SelectField, self).__init__(*args, **kwargs)

    def select(self, value=None, index=None, text=None):
        self.clog('select')
        # Execute first select instruction, then return
        if value is not None:
            return self.select_by_value(value)
        if index is not None:
            return self.select_by_index(index)
        if text is not None:
            return self.select_by_visible_text(text)
        Log.warning('Call to SelectField.select() with no arguments does nothing.')
        return True
