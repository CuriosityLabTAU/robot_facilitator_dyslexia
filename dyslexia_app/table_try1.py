from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        b=BoxLayout(orientation='vertical')
        t=TextInput(font_size=50,
                    size_hint_y=None,
                    height=50,
                    width=50,
                    text='default')
        l = Label(text='default', font_size=100)
        l2 = Label(text='default', font_size=100)

        t.bind(text=l.setter('text1'))
        b.add_widget(t)
        b.add_widget(l)
        b.add_widget(l2)


        return b

if __name__ == "__main__":
    TutorialApp().run()