from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

#from kivy_communication import *
from hebrew_management import *


class MyScreenManager (ScreenManager):
    the_app = None


class ScreenHebrew (Screen):
    the_app = None

    def __init__(self, the_app):
        self.the_app = the_app
        super(Screen, self).__init__()

        #self.ids["title"].text = "test"
        self.ids["text_1"].bind(text=HebrewManagement.text_change)
        self.ids["text_2"].bind(text=HebrewManagement.text_change)
        #self.ids["audience_list_group_2"].bind(text=HebrewManagement.text_change)
        #self.ids["audience_list_group_3"].bind(text=HebrewManagement.text_change)


class HebrewApp(App):  #The name of the class will make it search for robotator.kv
    def build(self):
        self.the_app = self
        self.screen_manager = MyScreenManager()
        screen_hebrew = ScreenHebrew(self)
        self.screen_manager.add_widget(screen_hebrew)
        self.screen_manager.current = 'ScreenHebrew'
        return self.screen_manager

if __name__ == "__main__":
    HebrewApp().run()  #the call is from main.py