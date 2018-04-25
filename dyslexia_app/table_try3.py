from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class table_try3App(App):
    def build(self):
        layout = GridLayout(cols=3, row_force_default=True, row_default_height=40)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(1,70):
            layout.add_widget(Button(text='Hello '+str(i), size_hint_x=None, width=100))
            layout.add_widget(Button(text='World '+str(i)))
            layout.add_widget(Button(text='?'))
        #return layout
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        return root

if __name__ == "__main__":
    table_try3App().run()