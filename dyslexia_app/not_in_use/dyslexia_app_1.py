# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner

from dyslexia_app.kivy_classes import *
from dyslexia_app.kivy_communication import *


class MyScreenManager(ScreenManager):
    the_app = None

class ScreenDyslexia (Screen):
    answers_single = []
    answers_tefel = []
    dyslexia_single_data = {}
    dyslexia_tefel_data = {}

    def __init__(self, the_app):
        self.the_app = the_app
        super(Screen, self).__init__()
        self.add_words_single()
        self.add_words_tefel()
        # self.ids["title"].text = "test"
        #self.ids["text_1"].bind(text=HebrewManagement.text_change)
        #self.ids["text_2"].bind(text=HebrewManagement.text_change)
        # self.ids["audience_list_group_2"].bind(text=HebrewManagement.text_change)
        # self.ids["audience_list_group_3"].bind(text=HebrewManagement.text_change)

    class SpinnerDyslexia (Spinner):
        def __init__ (self,the_app):
            super(SpinnerDyslexia, self).__init__()

    def add_words_single(self):
        layout = self.ids['gridlayout_single']
        with open('dyslexia_single.json') as data_file:
            dyslexia_single_data = json.load(data_file)

        single_length = len(dyslexia_single_data['word'])
        for i in range(single_length):
            word_i = dyslexia_single_data['word'][i]
            response_i = dyslexia_single_data['response'][i]
            print(word_i, response_i)
            lbl_response = LabelB(text=response_i[::-1])
            lbl_word = LabelB(id='word' + str(i), text=word_i[::-1])  # , size_hint_y=None, height=20)
            # btn_response = Button(text=str(response_i), size_hint_y=None, height=40)
            spinner = SpinnerDyslexia(id='s'+str(i), sync_height = True,
                                    font_name= 'fonts/the_font.ttf', values= ('1','2','3','4'),
                                    height=16)
            layout.add_widget(spinner)
            layout.add_widget(lbl_response)
            layout.add_widget(lbl_word)
            #self.ids['word' + str(i)].bind(text=HebrewManagement.text_change)

    def add_words_tefel(self):
        layout = self.ids['gridlayout_tefel']
        with open('dyslexia_tefel.json') as data_file:
            dyslexia_tefel_data = json.load(data_file)
        tefel_length = len(dyslexia_tefel_data['word'])
        for i in range(tefel_length):
            word_i = dyslexia_tefel_data['word'][i]
            response_i = dyslexia_tefel_data['response'][i]
            print(word_i, response_i)
            lbl_response = LabelB(text=response_i[::-1])
            lbl_word = LabelB(id='word' + str(i), text=word_i[::-1])  # , size_hint_y=None, height=20)
            # btn_response = Button(text=str(response_i), size_hint_y=None, height=40)
            spinner = SpinnerDyslexia(id='s' + str(i), sync_height=True, text = 'test',
                                      font_name='fonts/the_font.ttf', values=('1', '2', '3', '4'),
                                      height=16)
            layout.add_widget(spinner)
            layout.add_widget(lbl_response)
            layout.add_widget(lbl_word)

            # self.ids['word' + str(i)].bind(text=HebrewManagement.text_change)

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
        screen_dyslexia = ScreenDyslexia(self)
        self.screen_manager.add_widget(screen_dyslexia)
        self.screen_manager.current = 'ScreenDyslexia'
        return self.screen_manager


    def condition_selected(self,):
        # NOW MOVED TO ADD AND NAMED condition_selection
        print("condition_selected app")
        # condition = self.screen_manager.get_screen('zero_screen_room').ids['condition_spinner'].text
        # self.the_app.update_condition(condition)
        # self.update_condition(condition)
        print('text,id')
    def on_toggle_btn(self, screen_name):
        print ('state:', 'screen_name',screen_name)

    def change_screen(self, screen_name):
        print ('state:', 'screen_name', screen_name)
        if (screen_name == 'single'):
            self.screen_manager.get_screen('ScreenDyslexia').ids['single_content'].opacity = 1
            self.screen_manager.get_screen('ScreenDyslexia').ids['tefel_content'].opacity = 0
        elif (screen_name == 'tefel'):
            self.screen_manager.get_screen('ScreenDyslexia').ids['single_content'].opacity = 0
            self.screen_manager.get_screen('ScreenDyslexia').ids['tefel_content'].opacity = 1
        elif (screen_name == 'summary'):
            self.screen_manager.get_screen('ScreenDyslexia').ids['single_content'].opacity = 0
            self.screen_manager.get_screen('ScreenDyslexia').ids['tefel_content'].opacity = 0

        #self.screen_manager.current = screen_name

if __name__ == "__main__":
    DyslexiaApp().run()  # the call is from main.py