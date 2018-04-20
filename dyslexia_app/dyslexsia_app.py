import json
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

layout = GridLayout(cols=2, spacing=1, size_hint_y=None)
# Make sure the height is such that there is something to scroll.
layout.bind(minimum_height=layout.setter('height'))
# Read JSON file
with open('dyslexia_single.json') as data_file:
    dyslexia_single_data = json.load(data_file)

for i in range(len(dyslexia_single_data['word'])):
    word_i = dyslexia_single_data['word'][i]
    response_i = dyslexia_single_data['response'][i]
    print(word_i,response_i)
    lbl_word = Label(font_name='fonts/OpenSansHebrew-Bold.ttf', text=word_i, size_hint_y=None, height=40)
    lbl_response = Label(font_name='fonts/the_font.ttf', text=response_i, size_hint_y=None, height=40)
    #btn_response = Button(text=str(response_i), size_hint_y=None, height=40)
    layout.add_widget(lbl_word)
    layout.add_widget(lbl_response)
root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)

runTouchApp(root)




#class TutorialApp(App):
#    def build(self):
#        layout = GridLayout(cols=3, row_force_default=True, row_default_height=40)
#        for i in range(1,20):
#            layout.add_widget(Button(text='Hello '+str(i), size_hint_x=None, width=100))
#            layout.add_widget(Button(text='World '+str(i)))
 #           layout.add_widget(Button(text='?'))
#        #return layout
#        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
#        root.add_widget(layout)
#        return root

#if __name__ == "__main__":
 #   TutorialApp().run()