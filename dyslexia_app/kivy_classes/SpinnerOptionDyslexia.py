from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.spinner import SpinnerOption

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<SpinnerOptionDyslexia>:
  color: 1, 1, 1, 1
  size_hint_y: None
  height: '40dp'
  text: 'rinat'
  font_size: '20sp'
  font_name: 'fonts/the_font.ttf'
""")

class SpinnerOptionDyslexia(SpinnerOption):
  #def __init__(self):
  #  super(SpinnerOptionButtonDyslexia, self).__init__()
  color = (1,1,1,1)

Factory.register('KivyB', module='SpinnerOptionDyslexia')