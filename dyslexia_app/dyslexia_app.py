# -*- coding: utf-8 -*-

import numpy as np
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from kivy_classes import *
from kivy_communication import *

from kivy.properties import ListProperty, ObjectProperty, BooleanProperty

class MyScreenManager(ScreenManager):
    the_app = None

class ScreenDyslexia (Screen):
    answers_single1 = []
    answers_single2 = []
    answers_tefel1 = []
    answers_tefel2 = []
    dyslexia_single_data = {}
    dyslexia_tefel_data = {}
    dyslexia_single_mistakes = {}
    dyslexia_tefel_mistakes = {}
    dyslexia_types = {}
    single_mistakes_length = 0
    tefel_mistakes_length = 0
    single_length = 0
    tefel_length = 0

    def __init__(self, the_app):
        #init the app. Set the tab to be single words
        self.the_app = the_app
        super(Screen, self).__init__()
        self.read_json_data ()
        self.init_variables ()
        self.reverse_mistakes_text()
        self.create_task_grid('single')
        self.create_task_grid('tefel')
        self.create_diagnosis_grid()
        #self.create_single_grid() #init layout_single
        #self.create_tefel_grid()  #init layout_tefel
        self.ids['scroll_content'].add_widget(self.layout_single)
        self.current_tab = 'single'

    def read_json_data(self):
        #read the json files that contain the single and tefel words tasks
        with open('dyslexia_single.json') as data_file:
            self.dyslexia_single_data = json.load(data_file)
        with open('dyslexia_tefel.json') as data_file:
            self.dyslexia_tefel_data = json.load(data_file)
        with open('dyslexia_single_mistakes.json') as data_file:
            self.dyslexia_single_mistakes = json.load(data_file)
        with open('dyslexia_tefel_mistakes.json') as data_file:
            self.dyslexia_tefel_mistakes = json.load(data_file)
        with open('dyslexia_types.json') as data_file:
            self.dyslexia_types = json.load(data_file)


    def init_variables(self):
        #init the variables of the study
        self.single_length = len(self.dyslexia_single_data['word'])
        self.tefel_length = len(self.dyslexia_tefel_data['word'])
        self.answers_tefel1 = np.zeros(self.single_length)-1
        self.answers_tefel2 = np.zeros(self.single_length)-1
        self.single_mistakes_length = len(self.dyslexia_single_mistakes['initials'])
        self.tefel_mistakes_length = len(self.dyslexia_tefel_mistakes['initials'])
        self.answers_single1 = np.zeros(self.single_length)-1
        self.answers_single2 = np.zeros(self.single_length)-1
        self.answers_single_summary = np.zeros(self.single_mistakes_length)
        self.answers_tefel_summary = np.zeros(self.tefel_mistakes_length)

    def reverse_mistakes_text(self):
        #reverse the hebrew letters in the mistakes initials list and dyslexia type list
        #so they will look right
        for i in range(self.single_mistakes_length):
            initials_i = self.dyslexia_single_mistakes['initials'][i]
            mistakes_i = self.dyslexia_single_mistakes['mistakes'][i]
            self.dyslexia_single_mistakes['initials'][i] = initials_i[::-1]
            self.dyslexia_single_mistakes['mistakes'][i] = mistakes_i[::-1]

        for i in range(self.tefel_mistakes_length):
            word_i = self.dyslexia_tefel_mistakes['initials'][i]
            mistakes_i = self.dyslexia_tefel_mistakes['mistakes'][i]
            self.dyslexia_tefel_mistakes['initials'][i] = self.dyslexia_tefel_mistakes['initials'][i][::-1]
            self.dyslexia_tefel_mistakes['mistakes'][i] = mistakes_i[::-1]

        for i in range(len(self.dyslexia_types['dyslexia_types'])):
            type_i = self.dyslexia_types['dyslexia_types'][i]
            self.dyslexia_types['dyslexia_types'][i] = type_i[::-1]


    def create_diagnosis_grid(self):
        self.layout_diagnosis = GridLayoutDyslexia(cols=2)
        lbl_head1 = LabelHeadingDyslexia(text='הריחב') #,size_hint_x=None, width=300)
        lbl_head0 = LabelHeadingDyslexia(text='היסקלסיד', halign='right')
        self.layout_diagnosis.add_widget(lbl_head0)
        self.layout_diagnosis.add_widget(lbl_head1)
        for dyslexia in self.dyslexia_types['dyslexia_types']:
            lbl_type = LabelDyslexia(text = dyslexia)
            checkbox = CheckBoxDyslexia ()#(size_hint_x=None, width=300)
            self.layout_diagnosis.add_widget(lbl_type)
            self.layout_diagnosis.add_widget(checkbox)


    def create_task_grid(self, task_name):
        # Create GridLayoutDyslexia inst that will be used whenever the single tab  or the tegel tab is pressed is pressed.
        # task_name = 'single' / 'tefel'
        lbl_head0 = LabelHeadingDyslexia(text='הרזע')
        lbl_head1 = LabelHeadingDyslexia(text='?תפסונ האיגש')
        lbl_head2 = LabelHeadingDyslexia(text='האיגש גוס')
        lbl_head3 = LabelHeadingDyslexia(text='הבוגת')
        lbl_head4 = LabelHeadingDyslexia(text='הלימ')

        if (task_name=='single'):
            self.layout_single = GridLayoutDyslexia()
            self.dyslexia_data = self.dyslexia_single_data
            self.dyslexia_mistakes = self.dyslexia_single_mistakes
            self.task_length = self.single_length
            self.layout_single.add_widget(lbl_head0)
            self.layout_single.add_widget(lbl_head1)
            self.layout_single.add_widget(lbl_head2)
            self.layout_single.add_widget(lbl_head3)
            self.layout_single.add_widget(lbl_head4)
            prefix = 's'
        elif (task_name=='tefel'):
            self.layout_tefel = GridLayoutDyslexia()
            self.dyslexia_data = self.dyslexia_tefel_data
            self.dyslexia_mistakes = self.dyslexia_tefel_mistakes
            self.task_length = self.tefel_length
            self.layout_tefel.add_widget(lbl_head0)
            self.layout_tefel.add_widget(lbl_head1)
            self.layout_tefel.add_widget(lbl_head2)
            self.layout_tefel.add_widget(lbl_head3)
            self.layout_tefel.add_widget(lbl_head4)
            prefix = 't'

        for i in range(self.task_length):
            word_i = self.dyslexia_data['word'][i]
            response_i = self.dyslexia_data['response'][i]
            #print(word_i, response_i)
            lbl_response = LabelDyslexia(text=response_i[::-1]) #reverse the string
            lbl_word = LabelDyslexia(id='word' + str(i), text= word_i[::-1] + ' .'+ str(i)) #reverse the string
            # btn_response = Button(text=str(response_i), size_hint_y=None, height=40)
            spinner_values = self.dyslexia_mistakes['initials']
            if (response_i=='1'):  #the response in the test is corrent
                spinner1 = LabelDyslexia(text='')
                spinner2 = LabelDyslexia(text='')
                btn_question = LabelDyslexia(text='')

            else: #the response in the dyslexia test is incorrect
                spinner1 = SpinnerDyslexia(id=prefix + '1_' + str(i),
                                           sync_height=True,
                                           text='י/רחב',
                                           values=spinner_values,
                                           option_cls=SpinnerOptionDyslexia)
                spinner2 = SpinnerDyslexia(id=prefix + '2_' + str(i),
                                           sync_height=True,
                                           text='י/רחב',
                                           values=spinner_values,
                                           option_cls=SpinnerOptionDyslexia)
                btn_question = ButtonDyslexia (id=prefix + str(i),
                                               text='?')

            if (task_name == 'single'):
                self.layout_single.add_widget(btn_question)
                self.layout_single.add_widget(spinner2)
                self.layout_single.add_widget(spinner1)
                self.layout_single.add_widget(lbl_response)
                self.layout_single.add_widget(lbl_word)
            elif (task_name == 'tefel'):
                self.layout_tefel.add_widget(btn_question)
                self.layout_tefel.add_widget(spinner2)
                self.layout_tefel.add_widget(spinner1)
                self.layout_tefel.add_widget(lbl_response)
                self.layout_tefel.add_widget(lbl_word)

    def create_summary_grid(self):
        #create the summary gird layout that includes single and tefel
        self.layout_summary = GridLayoutDyslexia(cols=4)
        # add single summary:
        self.add_summary_data(':תודדוב םוכיס',self.dyslexia_single_mistakes,self.single_mistakes_length,self.answers_single_summary)
        #add tefel summary:
        self.add_summary_data(':לפת םוכיס',self.dyslexia_tefel_mistakes,self.tefel_mistakes_length,self.answers_tefel_summary)

    def add_summary_data(self, title_text ,dyslexia_mistakes, mistakes_length,answers_summary):


        lbl_head0 = LabelHeadingDyslexia(text='לכה ךס')
        lbl_head1 = LabelHeadingDyslexia(text='דודיק')
        lbl_head2 = LabelHeadingDyslexia(text='האיגש גוס')
        lbl_head3 = LabelHeadingDyslexia(text=title_text)
        self.layout_summary.add_widget(lbl_head0)
        self.layout_summary.add_widget(lbl_head1)
        self.layout_summary.add_widget(lbl_head2)
        self.layout_summary.add_widget(lbl_head3)


        for i in range(mistakes_length):

            mistake_id = str(int(i+1))
            mistake_type = dyslexia_mistakes['mistakes'][i]
            mistake_initials = dyslexia_mistakes['initials'][i]
            mistake_count = str(int(answers_summary[i]))

            lbl_mistake_count = LabelDyslexia(text=mistake_count)
            lbl_mistake_initials = LabelDyslexia(text=mistake_initials)
            lbl_mistake_type = LabelDyslexia(text=mistake_type)
            lbl_mistake_id = LabelDyslexia(text=mistake_id)

            self.layout_summary.add_widget(lbl_mistake_count)
            self.layout_summary.add_widget(lbl_mistake_initials)
            self.layout_summary.add_widget(lbl_mistake_type)
            self.layout_summary.add_widget(lbl_mistake_id)

class DyslexiaApp(App):
    def build(self):
        self.the_app = self
        self.screen_manager = MyScreenManager()
        screen_dyslexia = ScreenDyslexia(self)
        self.screen_manager.add_widget(screen_dyslexia)
        self.screen_manager.current = 'ScreenDyslexia'
        return self.screen_manager

    def mistake_type_selected(self,spinner_inst):
        # the student picked mistake type. update the relevant variables
        screen_dyslexia = self.screen_manager.get_screen('ScreenDyslexia')

        selection_id = spinner_inst.id #id of the spinner. e.g.:"s1_0" = single, first column mistake, word 0
        task_name = selection_id[0] #'s'/'t'
        column_name = selection_id[1] #'1'/'2'
        word_index = int(selection_id[3:]) #0-17

        if (task_name=='s'): #single task
            mistake_index = screen_dyslexia.dyslexia_single_mistakes['initials'].index(spinner_inst.text)
            if (column_name=='1'): #first column
                if (screen_dyslexia.answers_single1[word_index]>=0):
                        prev_selection = screen_dyslexia.answers_single1[word_index]
                        screen_dyslexia.answers_single_summary[prev_selection] -= 1
                screen_dyslexia.answers_single1[word_index] = mistake_index
            else: #selcond column
                if (screen_dyslexia.answers_single2[word_index] >= 0):
                    prev_selection = screen_dyslexia.answers_single2[word_index]
                    screen_dyslexia.answers_single_summary[prev_selection] -= 1
                screen_dyslexia.answers_single2[word_index] = mistake_index
            screen_dyslexia.answers_single_summary[mistake_index] += 1
        elif (task_name=='t'): #tefel task
            mistake_index = screen_dyslexia.dyslexia_tefel_mistakes['initials'].index(spinner_inst.text)
            if (column_name=='1'): #first column
                if (screen_dyslexia.answers_tefel1[word_index] >= 0):
                    prev_selection = screen_dyslexia.answers_tefel1[word_index]
                    screen_dyslexia.answers_tefel_summary[prev_selection] -= 1
                screen_dyslexia.answers_tefel1[word_index] = mistake_index
            else: #selcond column
                if (screen_dyslexia.answers_tefel2[word_index] >= 0):
                    prev_selection = screen_dyslexia.answers_tefel1[word_index]
                    screen_dyslexia.answers_tefel_summary[prev_selection] -= 1
                screen_dyslexia.answers_tefel2[word_index] = mistake_index
            screen_dyslexia.answers_tefel_summary[mistake_index] += 1

        print(task_name, column_name, word_index, selection_id, mistake_index)


    def change_tab(self, tab_name):
        # student clicked on one of the menu tabs ('single'/'tefel'/'summary')
        print ('state:', 'screen_name', tab_name)
        if (tab_name == 'single'):
            self.current_tab = 'single'
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].add_widget(self.screen_manager.get_screen('ScreenDyslexia').layout_single)
        elif (tab_name == 'tefel'):
            self.current_tab = 'tefel'
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].add_widget(self.screen_manager.get_screen('ScreenDyslexia').layout_tefel)
        elif (tab_name == 'summary'):
            self.current_tabe = 'summary'
            self.screen_manager.get_screen('ScreenDyslexia').create_summary_grid()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].add_widget(self.screen_manager.get_screen('ScreenDyslexia').layout_summary)
        elif (tab_name == 'diagnosis'):
            self.current_tabe = 'diagnosis'
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].clear_widgets()
            self.screen_manager.get_screen('ScreenDyslexia').ids['scroll_content'].add_widget(self.screen_manager.get_screen('ScreenDyslexia').layout_diagnosis)

if __name__ == "__main__":
    DyslexiaApp().run()  # the call is from main.py