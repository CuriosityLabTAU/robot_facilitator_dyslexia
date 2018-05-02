# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_classes import *
from kivy_communication import *
from kivy.properties import ListProperty, ObjectProperty, BooleanProperty

class MyScreenManager(ScreenManager):
    the_app = None

class ScreenDyslexia (Screen):
    answers_single = []
    answers_tefel = []
    dyslexia_single_data = {}
    dyslexia_tefel_data = {}
    single_length = 0
    tefel_length = 0

    def __init__(self, the_app):
        #init the app. Set the tab to be single words
        self.the_app = the_app
        super(Screen, self).__init__()
        self.read_json_data ()
        self.create_single_grid() #init layout_single
        self.create_tefel_grid()  #init layout_tefel
        self.ids['scroll_content'].add_widget(self.layout_single)
        self.current_tab = 'single'

    def read_json_data(self):
        #read the json files that contain the single and tefel words tasks
        with open('dyslexia_single.json') as data_file:
            self.dyslexia_single_data = json.load(data_file)
        self.single_length = len(self.dyslexia_single_data['word'])

        with open('dyslexia_tefel.json') as data_file:
            self.dyslexia_tefel_data = json.load(data_file)
        self.tefel_length = len(self.dyslexia_tefel_data['word'])

    def create_single_grid(self):
        #Create GridLayoutDyslexia inst that will be used whenever the single tab is pressed.
        self.layout_single = GridLayoutDyslexia()

        lbl_head1 = LabelHeadingDyslexia(text ='תועט גוס')
        lbl_head2 = LabelHeadingDyslexia(text ='הבוגת')
        lbl_head3 = LabelHeadingDyslexia(text = 'הלימ')

        self.layout_single.add_widget(lbl_head1)
        self.layout_single.add_widget(lbl_head2)
        self.layout_single.add_widget(lbl_head3)

        for i in range(self.single_length):
            word_i = self.dyslexia_single_data['word'][i]
            response_i = self.dyslexia_single_data['response'][i]
            print(word_i, response_i)
            lbl_response = LabelDyslexia(text=response_i[::-1])
            lbl_word = LabelDyslexia(id='word' + str(i), text=word_i[::-1])  # , size_hint_y=None, height=20)
            # btn_response = Button(text=str(response_i), size_hint_y=None, height=40)
            spinner_values = ('1', '2', '3', '4', '5', '6', '7', '8', '9','10')
            spinner = SpinnerDyslexia(id='s'+str(i), sync_height = True, text='?',
                                    font_name= 'fonts/the_font.ttf', values= spinner_values,
                                    height=16)
            self.layout_single.add_widget(spinner)
            self.layout_single.add_widget(lbl_response)
            self.layout_single.add_widget(lbl_word)


    def create_tefel_grid(self):
        self.layout_tefel = GridLayoutDyslexia()

        lbl_head1 = LabelHeadingDyslexia(text ='תועט גוס')
        lbl_head2 = LabelHeadingDyslexia(text ='הבוגת')
        lbl_head3 = LabelHeadingDyslexia(text = 'הלימ')
        self.layout_tefel.add_widget(lbl_head1)
        self.layout_tefel.add_widget(lbl_head2)
        self.layout_tefel.add_widget(lbl_head3)
        for i in range(self.tefel_length):
            word_i = self.dyslexia_tefel_data['word'][i]
            response_i = self.dyslexia_tefel_data['response'][i]
            print(word_i, response_i)
            lbl_response = LabelDyslexia(text=response_i[::-1])
            lbl_word = LabelDyslexia(id='word' + str(i), text=word_i[::-1])  # , size_hint_y=None, height=20)
            # btn_response = Button(text=str(response_i), size_hint_y=None, height=40)

            spinner = SpinnerDyslexia(id='s' + str(i), sync_height=True, text = '?',
                                      font_name='fonts/the_font.ttf', values=('1', '2', '3', '4'),
                                      height=16)
            self.layout_tefel.add_widget(spinner)
            self.layout_tefel.add_widget(lbl_response)
            self.layout_tefel.add_widget(lbl_word)

    def add_spinner(self):
        spinner = LoggedSpinner (id= 'condition_spinner', text= 'condition', font_size= 16,
                                 background_color= (0.2,0.2,0.2,1), font_name= 'fonts/the_font.ttf', values= ('1','2','3','4'), height=20)
        return spinner

class DyslexiaApp(App):
    def build(self):
        self.the_app = self
        self.screen_manager = MyScreenManager()
        screen_dyslexia = ScreenDyslexia(self)
        self.screen_manager.add_widget(screen_dyslexia)
        self.screen_manager.current = 'ScreenDyslexia'
        return self.screen_manager

    def mistake_type_selected(self,spinner_inst):
        # NOW MOVED TO ADD AND NAMED condition_selection
        print(spinner_inst.id)
        print("condition_selected app")
        #condition = self.screen_manager.get_screen('ScreenDyslexia').ids['condition_spinner'].text
        # self.the_app.update_condition(condition)
        # self.update_condition(condition)
        print('text,id')

    def on_toggle_btn(self, screen_name):
        print ('state:', 'screen_name',screen_name)

    def change_screen(self, screen_name):
        print ('state:', 'screen_name', screen_name)
        if (screen_name == 'single'):
            self.current_tab = 'single'
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].add_widget(self.screen_manager.get_screen('ScreenDyslexia').layout_single)
        elif (screen_name == 'tefel'):
            self.current_tab = 'tefel'
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].add_widget(self.screen_manager.get_screen('ScreenDyslexia').layout_tefel)
        elif (screen_name == 'summary'):
            self.current_tabe = 'summary'
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()

        #self.screen_manager.current = screen_name

if __name__ == "__main__":
    DyslexiaApp().run()  # the call is from main.py