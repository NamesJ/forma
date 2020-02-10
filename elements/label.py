from . import TextBox
from . import ClickBox


class Label (TextBox, ClickBox):
    def __init__(self, *args, **kwargs):
        super(Label, self).__init__(*args, **kwargs)
