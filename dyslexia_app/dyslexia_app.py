import json
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.app import App
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from hebrew_management import *
from kivy_classes import *
from kivy_communication import *
from kivy.uix.spinner import Spinner


class MyScreenManager(ScreenManager):
    the_app = None


class ScreenDyslexiaSingle (Screen):

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
                lbl_response = LabelB(text=response_i[::-1])
                lbl_word = LabelB(id='word' + str(i), text=word_i[::-1])  # , size_hint_y=None, height=20)
                # btn_response = Button(text=str(response_i), size_hint_y=None, height=40)
                spinner = Spinner(id='condition_spinner', text='type', font_size=16, sync_height = True,
                                        background_color=(0, 0, 0, 1), font_name= 'fonts/the_font.ttf', values= ('1','2','3','4'), height=20, on_text= self.the_app.condition_selected)
                layout.add_widget(spinner)
                layout.add_widget(lbl_response)
                layout.add_widget(lbl_word)
                #self.ids['word' + str(i)].bind(text=HebrewManagement.text_change)

        def add_spinner(self):
            spinner = LoggedSpinner (id= 'condition_spinner', text= 'condition', font_size= 16,
                                     background_color= (0.2,0.2,0.2,1), font_name= 'fonts/the_font.ttf', values= ('1','2','3','4'), height=20)
            return spinner

class DyslexiaApp(App):
    def build(self):
        #layout = GridLayout(cols=3, row_force_default=True, row_default_height=40)
        #for i in range(1,20):
        #    layout.add_widget(Button(text='Hello '+str(i), size_hint_x=None, width=100))
        #    layout.add_widget(Button(text='World '+str(i)))
        #    layout.add_widget(Button(text='?'))

        self.the_app = self
        self.screen_manager = MyScreenManager()
        screen_dyslexia_single = ScreenDyslexiaSingle(self)
        self.screen_manager.add_widget(screen_dyslexia_single)
        self.screen_manager.current = 'ScreenDyslexiaSingle'
        return self.screen_manager

    def condition_selected(self):
        # NOW MOVED TO ADD AND NAMED condition_selection
        print("condition_selected")
        #condition = self.screen_manager.get_screen('zero_screen_room').ids['condition_spinner'].text
        # self.the_app.update_condition(condition)
        #self.update_condition(condition)
        print('text,id')

    def on_toggle_btn(self, screen_name):
        print ('state:', 'screen_name',screen_name)

    def change_screen(self, screen_name):
        print ('state:', 'screen_name', screen_name)
        if (screen_name == 'single'):
            self.screen_manager.get_screen('ScreenDyslexiaSingle').ids['single_content'].opacity = 1
        elif (screen_name == 'tefel'):
            self.screen_manager.get_screen('ScreenDyslexiaSingle').ids['single_content'].opacity = 0
        elif (screen_name == 'summary'):
            self.screen_manager.get_screen('ScreenDyslexiaSingle').ids['single_content'].opacity = 0



        #self.screen_manager.current = screen_name

if __name__ == "__main__":
    DyslexiaApp().run()  # the call is from main.py