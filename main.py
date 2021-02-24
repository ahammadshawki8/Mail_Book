# All imports 
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import NoTransition
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.base import runTouchApp
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
import webbrowser as web

# Setting up few things
Config.set('graphics', 'height', 680)
Config.set('graphics', 'width', 380)
Config.set('graphics', 'resizable', 0)
Config.write()

# Common Functions
def go_to_website():
    web.open_new_tab("https://ahammadshawki8.github.io/")



# Get Started
class GetStarted(Screen):
    def go_to_MainPanel(self):
        sm.add_widget(MainPanel(name="MainPanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "MainPanel"


# Main Panel
class MainPanel(Screen):
    def go_to_website(self):
        go_to_website()

    def go_to_AddPanel(self):
        sm.add_widget(AddPanel(name="AddPanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "AddPanel"

    def go_to_UpdatePanel(self):
        sm.add_widget(UpdatePanel(name="UpdatePanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "UpdatePanel"

    def go_to_DeletePanel(self):
        sm.add_widget(DeletePanel(name="DeletePanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "DeletePanel"

    def go_to_SearchPanel(self):
        sm.add_widget(SearchPanel(name="SearchPanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "SearchPanel"

    def go_to_SendPanel(self):
        sm.add_widget(SearchPanel(name="SearchPanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "SearchPanel"


# AddPanel Class
class AddPanel(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.9, 0.4
        self.info_grid.pos_hint = {"x": 0.05, "top": 0.65}
        self.time_label = Button(text = "Meeting Time:", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.time_label)
        self.time_value = TextInput(text="HH:MM", multiline = False)
        self.info_grid.add_widget(self.time_value)
        self.meeting_id_label = Button(text = "Meeting ID:", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.meeting_id_label)
        self.meeting_id_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.meeting_id_value)
        self.passcode_label = Button(text = "Passcode:", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.passcode_label)
        self.passcode_value = TextInput(multiline = False, password = True)
        self.info_grid.add_widget(self.passcode_value)
        self.organizer_label = Button(text = "Organizer:", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.organizer_label)
        self.organizer_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.organizer_value)
        self.subject_label = Button(text = "Meeting Subject:", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.subject_label)
        self.subject_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.subject_value)
        self.meeting_link_label = Button(text = "Browsable Link:", font_size = 14, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.info_grid.add_widget(self.meeting_link_label)
        self.meeting_link_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.meeting_link_value)

        self.add_widget(self.info_grid)
        self.submit_button = Button(text = "Add Email", italic = True, font_size = 18, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.submit_button.size_hint = 0.4, 0.06
        self.submit_button.pos_hint = {"x":0.3,"top": 0.2}
        self.add_widget(self.submit_button)
        self.submit_button.bind(on_release = lambda x: self.write_to_json())

    def go_to_website(self):
        go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "AddPanel":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "MainPanel"





# Some tasks before the running the file
kv = Builder.load_file("frontend.kv")
sm = ScreenManager(transition = SlideTransition())
screens = [
    GetStarted(name="GetStarted")
    ]

for screen in screens:
    sm.add_widget(screen)
sm.current = "GetStarted"


# main class
class Mail_BookApp(App):
    def build(self):
        Window.clearcolor = (0.85,0.85,0.85,1)
        return sm


# Running the entire file
if __name__ == "__main__":
    Mail_BookApp().run()