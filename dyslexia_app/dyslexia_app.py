# -*- coding: utf-8 -*-

import numpy as np
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from kivy_classes import *
from kivy_communication import *
from dyslexia_screen_register import *
from dyslexia_screen_dyslexia import *

from kivy.properties import ListProperty, ObjectProperty, BooleanProperty

class MyScreenManager(ScreenManager):
    the_app = None


class DyslexiaApp(App):
    def build(self):
        self.the_app = self
        self.basic_server_ip = '192.168.0.10'
        self.server_ip_end = 0
        self.screen_manager = MyScreenManager()
        screen_dyslexia = ScreenDyslexia(self)
        screen_register = ScreenRegister(self)
        self.screen_manager.add_widget(screen_dyslexia)
        self.screen_manager.add_widget(screen_register)
        self.screen_manager.current = 'ScreenDyslexia'  #'ScreenRegister'
        #self.screen_manager.current = 'ScreenRegister'

        self.try_connection()
        return self.screen_manager

    # ==========================================================================
    # ==== communicatoin to twisted server  KC: KivyClient KL: KivyLogger=====
    # ==========================================================================

    def try_connection(self):
        server_ip = self.basic_server_ip + str(self.server_ip_end)
        KC.start(the_parents=[self], the_ip=server_ip)  # 127.0.0.1
        KL.start(mode=[DataMode.file, DataMode.communication, DataMode.ros], pathname=self.user_data_dir,
                 the_ip=server_ip)

    def failed_connection(self):
        self.server_ip_end += 1
        if self.server_ip_end < 9:
            self.try_connection()

    def success_connection(self):
        self.server_ip_end = 99
        # self.screen_manager.current = 'Screen2'

    def on_connection(self):
        KL.log.insert(action=LogAction.data, obj='RobotatorApp', comment='start')
        print("the client status on_connection ", KC.client.status)
        if (KC.client.status == True):
            self.screen_manager.get_screen('ScreenRegister').ids['callback_label'].text = 'connected'

    def register_tablet(self):
        tablet_id = self.screen_manager.current_screen.ids['tablet_id'].text
        group_id = self.screen_manager.current_screen.ids['group_id'].text
        message = {'tablet_to_manager': {'action': 'register_tablet',
                                         'parameters': {'group_id': group_id, 'tablet_id': tablet_id}}}
        message_str = str(json.dumps(message))
        print("register_tablet", message_str)
        KC.client.send_message(message_str)

    def data_received(self, data):
        print ("robotator_app: data_received", data)
        self.screen_manager.get_screen('ScreenRegister').ids['callback_label'].text = data
        try:
            json_data = [json.loads(data)]
        except:
            json_data = []
            spl = data.split('}{')
            print(spl)
            for k in range(0, len(spl)):
                the_msg = spl[k]
                if k > 0:
                    the_msg = '{' + the_msg
                if k < (len(spl) - 1):
                    the_msg = the_msg + '}'
                json_msg = json.loads(the_msg)
                json_data.append(json_msg)
                # print("data_received err", sys.exc_info())

        for data in json_data:
            print("data['action']", data['action'])
            if (data['action'] == 'registration_complete'):
                self.screen_manager.get_screen('ScreenRegister').data_received(data)
                print("registration_complete")

            if (data['action'] == 'show_screen'):
                print(data)
                self.screen_manager.current = data['screen_name']

                if 'role' in data:
                    self.screen_manager.current_screen.update_role_bias(role=data['role'], bias=int(data['bias']))

            if (data['action'] == 'start_timer'):
                self.screen_manager.current_screen.ids['timer_time'].start_timer(int(data['seconds']))

            if data['action'] == 'set_widget_text':
                self.screen_manager.current_screen.ids[data['widget_id']].text = data['text']


    # ==========================================================================
    # Interaction in ScreenDyslexia
    # ==========================================================================

    def mistake_type_selected(self,spinner_inst):
        # the student picked mistake type. update the relevant variables
        screen_dyslexia = self.screen_manager.get_screen('ScreenDyslexia')
        self.screen_manager.get_screen('ScreenDyslexia').mistake_type_selected(spinner_inst)

    def press_help_button(self,btn_inst):
        print("press_help_button",btn_inst.id)
        self.screen_manager.get_screen('ScreenDyslexia').press_help_button(btn_inst)

    def press_close_help(self):
        print("press_close_help")
        self.screen_manager.get_screen('ScreenDyslexia').press_close_help()

    def change_tab(self, tab_name):
        # student clicked on one of the menu tabs ('single'/'tefel'/'summary')
        print ('state:', 'screen_name', tab_name)
        self.screen_manager.get_screen('ScreenDyslexia').change_tab(tab_name)


if __name__ == "__main__":
    DyslexiaApp().run()  # the call is from main.py