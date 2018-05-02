import sys
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import ListProperty
DEFAULT_PADDING = 6


class AlignedTextInput(TextInput):
    halign = StringProperty('left')
    valign = StringProperty('top')
    multiline = False
    #super.background_color = ListProperty ([0,0,0,1])
    def is_hebrew (self, substring):
        for c in substring:
            if ord(c) >= 1424 and ord(c) <= 1514:
                return True
        return False
    def insert_text(self, substring, from_undo=False):
        if self.is_hebrew(substring):
            str = self.text
            str = substring + str
            return super(AlignedTextInput, self)._set_text(str)
        return super(AlignedTextInput, self).insert_text(substring, from_undo=from_undo)

    def on_text(self, instance, value):
        self.redraw()

    def on_size(self, instance, value):
        self.redraw()

    def redraw(self):
        """
        Note: This methods depends on internal variables of its TextInput
        base class (_lines_rects and _refresh_text())
        """

        try:
            self._refresh_text(self.text)

            max_size = max(self._lines_rects, key=lambda r: r.size[0]).size
            num_lines = len(self._lines_rects)

            px = [DEFAULT_PADDING, DEFAULT_PADDING]
            py = [DEFAULT_PADDING, DEFAULT_PADDING]

            if self.halign == 'center':
                d = (self.width - max_size[0]) / 2.0 - DEFAULT_PADDING
                px = [d, d]
            elif self.halign == 'right':
                px[0] = self.width - max_size[0] - DEFAULT_PADDING

            if self.valign == 'middle':
                d = (self.height - max_size[1] * num_lines) / 2.0 - DEFAULT_PADDING
                py = [d, d]
            elif self.valign == 'bottom':
                py[0] = self.height - max_size[1] * num_lines - DEFAULT_PADDING

            self.padding_x = px
            self.padding_y = py
        except:
            print ("AlignedTextInput: text_change - unexpected error:", sys.exc_info())