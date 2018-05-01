from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<LabelB>:
  bcolor: 235/255.0, 234/255.0,236/255.0, 1
  color: 0, 0, 0, 1
  size_hint_y: None
  height: 30
  font_size: 20
  font_name: 'fonts/the_font.ttf'
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

class LabelB(Label):
  bcolor = ListProperty([235/255.0, 234/255.0,236/255.0,1])

Factory.register('KivyB', module='LabelB')