from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.togglebutton import ToggleButton

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<ToggleButtonDyslexia>:
  color: 1, 1, 1, 1
  size_hint_y: None
  height: '40dp'
  font_size: '20sp'
  font_name: 'fonts/the_font.ttf'

""")

class ToggleButtonDyslexia(ToggleButton):
  pass

Factory.register('KivyB', module='ToggleButtonDyslexia')