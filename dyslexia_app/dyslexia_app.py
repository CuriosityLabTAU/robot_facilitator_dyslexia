import json
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.app import App
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from hebrew_management import *

class MyScreenManager(ScreenManager):
    the_app = None

class LabelB(Label):
    bcolor  = ListProperty([1,1,1,1])

class ScreenDyslexia(Screen):
        the_app = None

        def __init__(self, the_app):
            self.the_app = the_app
            super(Screen, self).__init__()
            self.add_words()
            # self.ids["title"].text = "test"
            #self.ids["text_1"].bind(text=HebrewManagement.text_change)
            #self.ids["text_2"].bind(text=HebrewManagement.text_change)
            # self.ids["audience_list_group_2"].bind(text=HebrewManagement.text_change)
            # self.ids["audience_list_group_3"].bind(text=HebrewManagement.text_change)

        def add_words(self):
            layout = self.ids['gridlayout_words']
            with open('dyslexia_single.json') as data_file:
                dyslexia_single_data = json.load(data_file)
            for i in range(len(dyslexia_single_data['word'])):
                word_i = dyslexia_single_data['word'][i]
                response_i = dyslexia_single_data['response'][i]
                print(word_i, response_i)
                lbl_word = LabelB(id='word'+str(i), bcolor=(1,0,0,1), font_name='fonts/the_font.ttf', text=word_i[::-1])#, size_hint_y=None, height=20)
                lbl_response = Label(font_name='fonts/the_font.ttf', text=response_i, size_hint_y=None, height=20)
                # btn_response = Button(text=str(response_i), size_hint_y=None, height=40)
                layout.add_widget(lbl_word)
                layout.add_widget(lbl_response)
                #self.ids['word' + str(i)].bind(text=HebrewManagement.text_change)




class DyslexiaApp(App):
    def build(self):
        #layout = GridLayout(cols=3, row_force_default=True, row_default_height=40)

        #for i in range(1,20):
        #    layout.add_widget(Button(text='Hello '+str(i), size_hint_x=None, width=100))
        #    layout.add_widget(Button(text='World '+str(i)))
        #    layout.add_widget(Button(text='?'))

        self.the_app = self
        self.screen_manager = MyScreenManager()
        screen_dyslexia = ScreenDyslexia(self)
        self.screen_manager.add_widget(screen_dyslexia)
        self.screen_manager.current = 'ScreenDyslexia'
        return self.screen_manager


if __name__ == "__main__":
    DyslexiaApp().run()  # the call is from main.py