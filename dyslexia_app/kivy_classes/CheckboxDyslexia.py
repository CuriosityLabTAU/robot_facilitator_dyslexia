from kivy.uix.checkbox import CheckBox
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<CheckBoxDyslexia>:
  bcolor: 235/255.0, 234/255.0,236/255.0, 1
  color: 0, 0, 0, 1
  size_hint_y: None
  size_hint_x: None
  width: 100
  height: '40dp'
  font_size: '18sp'
  font_name: 'fonts/the_font.ttf'
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")
class CheckBoxDyslexia(CheckBox):
  bcolor = ListProperty([1, 1, 1 ,1])

Factory.register('KivyB', module='CheckBoxDyslexia')