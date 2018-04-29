from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<LabelB>:
  bcolor: 0, 1, 1, 1
  color: 0, 0, 0, 1
  size_hint_y: None
  height: 30
  font_name: 'fonts/the_font.ttf'
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

class LabelB(Label):
  bcolor = ListProperty([0.1,0.2,0.4,1])

Factory.register('KivyB', module='LabelB')