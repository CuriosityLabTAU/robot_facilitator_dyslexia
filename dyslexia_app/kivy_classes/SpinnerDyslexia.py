from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.spinner import Spinner
from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<SpinnerDyslexia>:
    font_name: 'fonts/the_font.ttf'
    font_size: 16
    sync_height: True
    background_color: 1, 1, 1, 1
    values: ('1', '2', '3', '4')
    height:20
    on_text: app.mistake_type_selected(self)
""")

class SpinnerDyslexia(Spinner):
  bcolor = ListProperty([235/255.0, 234/255.0,236/255.0,1])

Factory.register('KivyB', module='SpinnerDyslexia')