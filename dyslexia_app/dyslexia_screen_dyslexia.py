# -*- coding: utf-8 -*-

import numpy as np
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from kivy_classes import *
from kivy_communication import *
from dyslexia_screen_register import *

from kivy.properties import ListProperty, ObjectProperty, BooleanProperty
#solve to hebrew adding messages problem:
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ScreenDyslexia (Screen):
    diagnosis_checklist = []
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
   # current_tab = 'single'

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
        with open('googlesheet_jsons/dyslexia_single.json') as data_file:
            self.dyslexia_single_data = json.load(data_file)
        with open('googlesheet_jsons/dyslexia_tefel.json') as data_file:
            self.dyslexia_tefel_data = json.load(data_file)
        with open('googlesheet_jsons/dyslexia_single_mistakes.json') as data_file:
            self.dyslexia_single_mistakes = json.load(data_file)
        with open('googlesheet_jsons/dyslexia_tefel_mistakes.json') as data_file:
            self.dyslexia_tefel_mistakes = json.load(data_file)
        with open('googlesheet_jsons/dyslexia_types.json') as data_file:
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



    def change_tab(self, tab_name):
        # student clicked on one of the menu tabs ('single'/'tefel'/'summary')
        print ('state:', 'screen_name', tab_name)
        if (tab_name == 'single'):
            self.current_tab = 'single'
            self.ids['scroll_content'].clear_widgets()
            self.ids['scroll_content'].add_widget(self.layout_single)
        elif (tab_name == 'tefel'):
            self.current_tab = 'tefel'
            self.ids['scroll_content'].clear_widgets()
            self.ids['scroll_content'].add_widget(self.layout_tefel)
        elif (tab_name == 'single_summary'):
            self.current_tab = 'single_summary'
            self.create_single_summary_grid()
            self.ids['scroll_content'].clear_widgets()
            self.ids['scroll_content'].add_widget(self.layout_summary)
        elif (tab_name == 'tefel_summary'):
            self.current_tab = 'tefel_summary'
            self.create_tefel_summary_grid()
            self.ids['scroll_content'].clear_widgets()
            self.ids['scroll_content'].add_widget(self.layout_summary)
        elif (tab_name == 'diagnosis'):
            self.current_tab = 'diagnosis'
            self.ids['scroll_content'].clear_widgets()
            self.ids['scroll_content'].add_widget(self.layout_diagnosis)

    def create_diagnosis_grid(self):
        self.layout_diagnosis = GridLayoutDyslexia2(cols=2)

        #lbl_head0 = LabelHeadingDyslexia(text='הקידב')
        lbl_head1 = LabelHeadingDyslexia(text='היסקלסיד', halign='right')
        lbl_head2 = LabelHeadingDyslexia(text='הריחב')  # ,size_hint_x=None, width=300)

        #self.layout_diagnosis.add_widget(lbl_head0)
        self.layout_diagnosis.add_widget(lbl_head1)
        self.layout_diagnosis.add_widget(lbl_head2)
        for i, dyslexia in enumerate(self.dyslexia_types['dyslexia_types']):
            lbl_type = LabelDyslexia(text = dyslexia)
            checkbox = CheckBoxDyslexia (on_press=self.diagnosis_checkbox)#(size_hint_x=None, width=300)
            checkbox.name = 'checkbox_' + str(i)
            #btn_question = ButtonDyslexia(id='d' + str(i),text='?')
            #self.layout_diagnosis.add_widget(btn_question)
            self.layout_diagnosis.add_widget(checkbox)
            self.layout_diagnosis.add_widget(lbl_type)
            self.diagnosis_checklist.append(False)

        lbl_type = LabelDyslexia(text="")
        btn_check = ButtonDyslexia(id='d_test' , text='הקידב')
        self.layout_diagnosis.add_widget(btn_check)
        self.layout_diagnosis.add_widget(lbl_type)


    def press_diagnosis_test(self,*args):
        print ("press_diagnosis_test")
        sound_list = []
        str_message =''
        for i, is_checked in enumerate(self.diagnosis_checklist):
            if is_checked:
                sound_list.append(self.file_full_path('D_'+str(i)))
                sound_list.append(self.file_full_path('a'+str(i)))
                str_message = str_message + str(self.dyslexia_types['dyslexia_types'][i]) + str(' :םתרחב')
                str_message = str_message + '\n'
                str_message = str_message + self.dyslexia_types['feedback'][i][::-1]
                str_message = str_message + '\n'

        sound_list.append(self.file_full_path('final'))

        if (self.the_app.condition == 'tablet'):
            self.ids['help_label'].text = str_message
            self.ids['help_widget'].opacity = 1
        elif (self.the_app.condition =='robot'):
            #self.ids['help_label'].text = str_message
            #self.ids['help_widget'].opacity = 1
            nao_message = {'tablet_to_manager': {'action': 'play_audio_file', 'parameters': sound_list}}
            nao_message_str = str(json.dumps(nao_message))
            print("robot help me please", nao_message_str)
            KC.client.send_message(nao_message_str)

    def diagnosis_checkbox(self, *args):
        i = int(args[0].name.split('_')[1])
        self.diagnosis_checklist[i] = not self.diagnosis_checklist[i]
        print('-----')
        print(i, self.diagnosis_checklist[i])
        KL.log.insert(action=LogAction.data, obj='diagnosis_checklist', comment=str(self.diagnosis_checklist))

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
            self.layout_tefel = GridLayoutDyslexia4()
            self.dyslexia_data = self.dyslexia_tefel_data
            self.dyslexia_mistakes = self.dyslexia_tefel_mistakes
            self.task_length = self.tefel_length
            self.layout_tefel.add_widget(lbl_head0)
            #self.layout_tefel.add_widget(lbl_head1)
            self.layout_tefel.add_widget(lbl_head2)
            self.layout_tefel.add_widget(lbl_head3)
            self.layout_tefel.add_widget(lbl_head4)
            prefix = 't'

        for i in range(self.task_length):
            word_i = self.dyslexia_data['word'][i]
            response_i = self.dyslexia_data['response'][i]
            #print(word_i, response_i)
            lbl_response = LabelDyslexia(text=response_i[::-1]) #reverse the string
            lbl_word = LabelDyslexia(id='word' + str(i), text= word_i[::-1] + ' .'+ str(i+1)) #reverse the string
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
                spinner1.bind(text=spinner1.on_spinner_text)
                spinner1.name = 'spinner_' + task_name + '_' + str(i) + '_1'

                spinner2 = SpinnerDyslexia(id=prefix + '2_' + str(i),
                                           sync_height=True,
                                           text='י/רחב',
                                           values=spinner_values,
                                           option_cls=SpinnerOptionDyslexia)
                spinner2.bind(text=spinner2.on_spinner_text)
                spinner2.name = 'spinner_' + task_name + '_' + str(i) + '_2'

                btn_question = ButtonDyslexia (id=prefix + str(i),
                                               text='?')
                btn_question.name = 'btn_question_' + task_name + '_' + str(i)

            if (task_name == 'single'):
                self.layout_single.add_widget(btn_question)
                self.layout_single.add_widget(spinner2)
                self.layout_single.add_widget(spinner1)
                self.layout_single.add_widget(lbl_response)
                self.layout_single.add_widget(lbl_word)
            elif (task_name == 'tefel'):
                self.layout_tefel.add_widget(btn_question)
                #self.layout_tefel.add_widget(spinner2)
                self.layout_tefel.add_widget(spinner1)
                self.layout_tefel.add_widget(lbl_response)
                self.layout_tefel.add_widget(lbl_word)

    def create_single_summary_grid(self):
        # create the summary gird layout that includes single and tefel
        self.layout_summary = GridLayoutDyslexia4()
        # add single summary:
        self.add_summary_data(':תודדוב םוכיס', self.dyslexia_single_mistakes, self.single_mistakes_length,
                              self.answers_single_summary)
        self.add_summary_summary_data(self.dyslexia_single_data, self.dyslexia_single_mistakes, self.single_mistakes_length,
                                      self.answers_single_summary)

    def create_tefel_summary_grid(self):
        # create the summary gird layout that includes single and tefel
        self.layout_summary = GridLayoutDyslexia4()
        # add tefel summary:
        self.add_summary_data(':לפת םוכיס', self.dyslexia_tefel_mistakes, self.tefel_mistakes_length,
                              self.answers_tefel_summary)
        self.add_summary_summary_data(self.dyslexia_tefel_data, self.dyslexia_tefel_mistakes, self.tefel_mistakes_length,
                                      self.answers_tefel_summary)


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




    def add_summary_summary_data(self, dyslexia_data, dyslexia_mistakes, mistakes_length, answers_summary):
        correct_answers = dyslexia_data['response'].count('1')
        total_answers = float(len(dyslexia_data['response']))
        mistakes_percent = round(((total_answers - correct_answers) / total_answers) * 100, 1)
        print("mistakes_percent", mistakes_percent, correct_answers, total_answers)
        self.add_summary_summary_line(str(mistakes_percent)+'%', '', 'תויועט זוחא', '')
        self.add_summary_summary_line(str(int(answers_summary[1]+answers_summary[2])), '', 'םילוכיש', '')

        kbak = str(int(answers_summary[1]+answers_summary[7]+answers_summary[9]+answers_summary[11]+answers_summary[14]))
        kbak1 = str(int(answers_summary[7] + answers_summary[9] + answers_summary[11] + answers_summary[14]))
        kbak2 = str(int(answers_summary[7] + answers_summary[9] + answers_summary[11]))
        kbak3 = str(int(answers_summary[1]))

        self.add_summary_summary_line(kbak,
                                      '',
                                      'קאבק',
                                      '')
        self.add_summary_summary_line(str(int(answers_summary[6]+answers_summary[8]+answers_summary[12]+answers_summary[13]))
                                      , '',
                                      'ילאוזיו'
                                      , '')
        fixes=0
        for str_res in dyslexia_data['response']: #count the number of fixes the student made
            if '1' in str_res and '1' != str_res:
                fixes +=1
        self.add_summary_summary_line(str(int(fixes)), '', 'םינוקית', '')

        self.add_summary_summary_line('', 'םירגובמ ףס', '', '')
        if (self.current_tab=='single_summary'):
            self.add_summary_summary_line(str(int(answers_summary[0])), '3', 'ריממ כ"הס', '?חטש םאה')

        self.add_summary_summary_line(kbak, '2', 'קאבק כ"הס', '?קאבק םאה')
        self.add_summary_summary_line(kbak1, '2', 'תנ ילב קאבק', '')
        self.add_summary_summary_line(kbak2, '1', 'בקשקו תנ ילב קאבק', '')
        self.add_summary_summary_line(kbak3, '1', 'תנ', '')

        self.add_summary_summary_line(str(int(answers_summary[2])), '2', 'ענ', 'LPD םאה')
        self.add_summary_summary_line(str(int(answers_summary[1]+answers_summary[2])), '2', 'ךותב תודידנ כהס', '')
        self.add_summary_summary_line(str(int(answers_summary[1]+answers_summary[2]+answers_summary[10])), '2', 'תולפכהו תודידנ', '')

        self.add_summary_summary_line(str(int(answers_summary[3])), '2', 'יבשק', 'יבשק םאה')
        self.add_summary_summary_line(str(int(answers_summary[3]-answers_summary[14])), '2', 'בקשק תוחפ יבשק', '')
        self.add_summary_summary_line(str(int(answers_summary[5]+answers_summary[6]+answers_summary[8]+answers_summary[12]+answers_summary[13])), '1', 'רחא ילאוזיו', 'רפאב/ילאוזיו םאה')


    def add_summary_summary_line (self,txt1,txt2,txt3,txt4):
        lbl_head0 = LabelHeadingDyslexia(text=txt1, bcolor=(228/256.0 , 196/256.0 , 253/256.0,1))
        lbl_head1 = LabelHeadingDyslexia(text=txt2, bcolor=(228/256.0 , 196/256.0 , 253/256.0,1))
        lbl_head2 = LabelHeadingDyslexia(text=txt3, bcolor=(228/256.0 , 196/256.0 , 253/256.0,1))
        lbl_head3 = LabelHeadingDyslexia(text=txt4, bcolor=(228/256.0 , 196/256.0 , 253/256.0,1))
        self.layout_summary.add_widget(lbl_head0)
        self.layout_summary.add_widget(lbl_head1)
        self.layout_summary.add_widget(lbl_head2)
        self.layout_summary.add_widget(lbl_head3)



    def mistake_type_selected(self, spinner_inst):
        # the student picked mistake type. update the relevant variables

        selection_id = spinner_inst.id  # id of the spinner. e.g.:"s1_0" = single, first column mistake, word 0
        task_name = selection_id[0]  # 's'/'t'
        column_name = selection_id[1]  # '1'/'2'
        word_index = int(selection_id[3:])  # 0-17



        if (task_name == 's'):  # single task
            mistake_index = self.dyslexia_single_mistakes['initials'].index(spinner_inst.text)
            if (column_name == '1'):  # first column
                if (self.answers_single1[word_index] >= 0):
                    prev_selection = self.answers_single1[word_index]
                    self.answers_single_summary[int(prev_selection)] -= 1
                self.answers_single1[word_index] = mistake_index
            else:  # selcond column
                if (self.answers_single2[word_index] >= 0):
                    prev_selection = self.answers_single2[word_index]
                    self.answers_single_summary[int(prev_selection)] -= 1
                self.answers_single2[word_index] = mistake_index
            self.answers_single_summary[mistake_index] += 1
        elif (task_name == 't'):  # tefel task
            mistake_index = self.dyslexia_tefel_mistakes['initials'].index(spinner_inst.text)
            if (column_name == '1'):  # first column
                if (self.answers_tefel1[word_index] >= 0):
                    prev_selection = self.answers_tefel1[word_index]
                    self.answers_tefel_summary[int(prev_selection)] -= 1
                self.answers_tefel1[word_index] = mistake_index
            else:  # selcond column
                if (self.answers_tefel2[word_index] >= 0):
                    prev_selection = self.answers_tefel1[word_index]
                    self.answers_tefel_summary[int(prev_selection)] -= 1
                self.answers_tefel2[word_index] = mistake_index
            self.answers_tefel_summary[mistake_index] += 1
        print(task_name, column_name, word_index, selection_id, mistake_index)
        KL.log.insert(action=LogAction.data, obj='answers_single1', comment=str(self.answers_single1))
        KL.log.insert(action=LogAction.data, obj='answers_single2', comment=str(self.answers_single2))
        KL.log.insert(action=LogAction.data, obj='answers_tefel1', comment=str(self.answers_tefel1))
        KL.log.insert(action=LogAction.data, obj='answers_tefel2', comment=str(self.answers_tefel2))



    def press_help_button(self, btn_inst):

        task = btn_inst.id[0]  # s/t
        if (task=='d'):
            self.press_diagnosis_test()
            return

        print("press_help_button", btn_inst.id)
        word_index = int(btn_inst.id[1:])
        print('word_index=', word_index)
        message1 = ''
        message2 = ''
        nao_message = ''
        file_name1 = ''
        file_name2 = ''
        answer1=-1
        answer2=-1

        if (task == 's'):
            answer1 = int(self.answers_single1[word_index])
            answer2 = int(self.answers_single2[word_index])

            print(self.dyslexia_single_data['answer1'][word_index])
            if (self.dyslexia_single_data['answer1'][word_index]!='none'):
                correct_answer1 = self.dyslexia_single_mistakes['initials'].index(self.dyslexia_single_data['answer1'][word_index][::-1])
            else:
                correct_answer1 = -1
            if (self.dyslexia_single_data['answer2'][word_index]!='none'):
                correct_answer2 = self.dyslexia_single_mistakes['initials'].index(self.dyslexia_single_data['answer2'][word_index][::-1])
            else:
                correct_answer2 = -1

            print('correct_answer1 ', str(correct_answer1),'correct_answer2',str(correct_answer2))
            print('answer1 2', answer1, answer2)
            if (answer1 >= 0):
                file_name_pre1 = 'M_' + str(answer1) #you choose ...
                print(self.dyslexia_single_mistakes['mistakes'][answer1])
                message1 =   str(self.dyslexia_single_mistakes['mistakes'][answer1]) + str(' :םתרחב')
                message1 = message1 + '\n'
                feedback = self.dyslexia_single_data['m_' + str(answer1)][word_index]
                file_name_feedback1 = 's_w'+str(word_index)+'_m'+str(answer1)
                if (feedback=='none'):
                    if (answer1 == correct_answer1):
                        feedback = self.dyslexia_single_data['m_correct'][word_index]
                        file_name_feedback1 = 'correct'
                    else:
                        feedback = self.dyslexia_single_data['m_other'][word_index]
                        file_name_feedback1 = 'other_response'+str(np.random.randint(1,8))
                message1 = message1 + feedback[::-1]
                nao_message = {'tablet_to_manager': {'action': 'play_audio_file',
                                                     'parameters': [self.file_full_path(file_name_pre1),
                                                                    self.file_full_path(file_name_feedback1)]}}
            if (answer2 >= 0 and answer1 >= 0):
                file_name_pre2 = 'M_' + str(answer2)  # you choose ...
                message2 = str(self.dyslexia_single_mistakes['mistakes'][answer2]) + str(' :םתרחבו')
                message2 = message2 + '\n'
                feedback = self.dyslexia_single_data['m_' + str(answer2)][word_index]
                file_name_feedback2 = 's_w'+str(word_index)+'_m'+str(answer2)
                if (feedback=='none'):
                    if (answer2 == correct_answer2):
                        feedback = self.dyslexia_single_data['m_correct'][word_index]
                        file_name_feedback1 = 'correct'
                    else:
                        feedback = self.dyslexia_single_data['m_other'][word_index]
                        file_name_feedback2 = 'other_response' + str(np.random.randint(1, 8))
                message2 = message2 + feedback[::-1]
                nao_message = {'tablet_to_manager': {'action': 'play_audio_file',
                                                     'parameters': [self.file_full_path(file_name_pre1),
                                                                    self.file_full_path(file_name_feedback1),
                                                                    self.file_full_path(file_name_pre2),
                                                                    self.file_full_path(file_name_feedback2)]}}

            if (answer2 >= 0 and answer1 < 0):
                file_name_pre2 = 'M_' + str(answer2)  # you choose ...
                message2 = str(self.dyslexia_single_mistakes['mistakes'][answer2]) + str(' :םתרחבו')
                message2 = message2 + '\n'
                feedback = self.dyslexia_single_data['m_' + str(answer2)][word_index]
                file_name_feedback2 = 's_w'+str(word_index)+'_m'+str(answer2)
                if (feedback=='none'):
                    if (answer2 == correct_answer2):
                        feedback = self.dyslexia_single_data['m_correct'][word_index]
                        file_name_feedback1 = 'correct'
                    else:
                        feedback = self.dyslexia_single_data['m_other'][word_index]
                        file_name_feedback2 = 'other_response' + str(np.random.randint(1, 8))
                message2 = message2 + feedback[::-1]
                nao_message = {'tablet_to_manager': {'action': 'play_audio_file',
                                                     'parameters': [self.file_full_path(file_name_pre2),
                                                                    self.file_full_path(file_name_feedback2)]}}


            if (answer1<0 and answer2<0):
                feedback = self.dyslexia_single_data['m_none'][word_index][::-1]
                message1 = feedback
                file_name_feedback1 = 'other_response'+str(np.random.randint(1,8))
                nao_message = {'tablet_to_manager': {'action': 'play_audio_file',
                                                     'parameters': [self.file_full_path(file_name_feedback1)]}}
        elif (task == 't'):
            answer1 = int(self.answers_tefel1[word_index])
            if (self.dyslexia_tefel_data['answer1'][word_index] != 'none'):
                correct_answer1 = self.dyslexia_tefel_mistakes['initials'].index(
                    self.dyslexia_tefel_data['answer1'][word_index][::-1])
            else:
                correct_answer1 = -1
            if (answer1 >= 0):
                file_name_pre1 = 'M_' + str(answer1)  # you choose ...
                print(self.dyslexia_single_mistakes['mistakes'][answer1])
                message1 = str(self.dyslexia_tefel_mistakes['mistakes'][answer1]) + str(' :םתרחב')
                message1 = message1 + '\n'
                feedback = self.dyslexia_tefel_data['m_' + str(answer1)][word_index]
                file_name_feedback1 = 's_w' + str(word_index) + '_m' + str(answer1)
                if (feedback == 'none'):
                    if (answer1 == correct_answer1):
                        feedback = self.dyslexia_tefel_data['m_correct'][word_index]
                        file_name_feedback1 = 'correct'
                    else:
                        feedback = self.dyslexia_tefel_data['m_other'][word_index]
                        file_name_feedback1 = 'other_response' + str(np.random.randint(1, 8))
                message1 = message1 + feedback[::-1]
            elif (answer1 < 0): # did not choose anything
                feedback = self.dyslexia_tefel_data['m_none'][word_index][::-1]
                message1 = feedback
                file_name_feedback1 = 'other_response' + str(np.random.randint(1, 8))


        print("message2",message2)
        self.ids['help_label'].text = message1 +'\n'+ message2
        print('help_widget', self.ids['help_widget'].pos)

        # If the condition is robot then play the relevant sound files. If the condition is tablet show the help message on screen
        if (self.the_app.condition == 'tablet'):
            self.ids['help_widget'].opacity = 1
        elif (self.the_app.condition == 'robot'):
            #self.ids['help_widget'].opacity = 1
            #message =  {'action': 'play_audio_file', 'parameters': ['/home/nao/naoqi/sounds/dyslexia/s_w15_m7.wav']}
            if (nao_message ==""): #this will happen if the student only selected the second column
                file_name_feedback1 = 'other_response' + str(np.random.randint(1, 8))
                nao_message = {'tablet_to_manager': {'action': 'play_audio_file',
                                                 'parameters': [self.file_full_path(file_name_feedback1)]}}

            nao_message_str = str(json.dumps(nao_message))
            print("robot help me please", nao_message_str)
            KC.client.send_message(nao_message_str)

        # self.screen_manager.get_screen('ScreenDyslexia').dyslexia_tefel_data


    def file_full_path(self, name):
        full_path = str('/home/nao/naoqi/sounds/dyslexia/'+str(name)+'.wav')
        return full_path

    def press_close_help(self):
        print("press_close_help")
        self.ids['help_widget'].opacity = 0
        # self.screen_manager.get_screen('ScreenDyslexia').ids['help_widget'].pos_hint= {'center_x': 0.5, 'y': 0.2}


    def data_received(self, data):
        print ("ScreenDyslexia: data_received", data)
        # self.the_app.screen_manager.current = 'ScreenAudience'
        print("end")
        # self.ids['callback_label'].text = data
