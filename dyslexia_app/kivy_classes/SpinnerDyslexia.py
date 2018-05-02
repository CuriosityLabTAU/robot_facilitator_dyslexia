from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.spinner import Spinner
from kivy.uix.spinner import SpinnerOption
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, BooleanProperty
import SpinnerOptionDyslexia

from kivy.uix.gridlayout import GridLayout

Builder.load_string("""
<SpinnerDyslexia>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    font_size: 20
    font_name: 'fonts/the_font.ttf'
    height: 20


""")
class SpinnerOptionDys(SpinnerOption):
  #def __init__(self):
  #  super(SpinnerOptionDys, self).__init__()

  color = (1,1,1,1)
  text = 'rina'
  #height = 40
  #height = '40dp'
  #size_hint_y = None

class SpinnerDyslexia(Spinner):
  # option_cls = ObjectProperty(SpinnerOptionButtonDyslexia)
  #option_cls = ObjectProperty(SpinnerOptionButtonDyslexia)
  option_cls = ObjectProperty(SpinnerOptionDys)
  pass

Factory.register('KivyB', module='SpinnerDyslexia')