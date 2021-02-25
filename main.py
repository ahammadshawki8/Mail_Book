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
import database
import mail

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
        sm.add_widget(SendPanel(name="SendPanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "SendPanel"


# AddPanel Class
class AddPanel(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.9, 0.4
        self.info_grid.pos_hint = {"x": 0.05, "top": 0.67}

        self.name_label = Button(text = "Fullname:", font_size = 14)
        self.info_grid.add_widget(self.name_label)
        self.name_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.name_value)
        self.email_label = Button(text = "Email Address:", font_size = 14)
        self.info_grid.add_widget(self.email_label)
        self.email_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.email_value)
        self.category_label = Button(text = "Category:", font_size = 14)
        self.info_grid.add_widget(self.category_label)
        self.category_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.category_value)

        self.add_widget(self.info_grid)
        self.submit_button = Button(text = "Add Email", font_size = 18, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.submit_button.size_hint = 0.4, 0.06
        self.submit_button.pos_hint = {"x":0.3,"top": 0.2}
        self.add_widget(self.submit_button)
        self.submit_button.bind(on_release = lambda x: self.add_mail_function())

    def add_mail_function(self):
        value_list = []
        value_list.append(self.name_value.text)
        value_list.append(self.email_value.text)
        value_list.append(self.category_value.text)
        try:
            if ("" in value_list):
                show_AddPanelFailPop()
            database.add_mail(value_list)
            show_AddPanelSuccessPop()
        except:
            show_AddPanelFailPop()
        self.name_value.text = ""
        self.email_value.text = ""
        self.category_value.text = ""

    def go_to_website(self):
        go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "AddPanel":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "MainPanel"


# Add Panel Success PopUp
class AddPanelSuccessPop(FloatLayout):
    pass

def show_AddPanelSuccessPop():
    show = AddPanelSuccessPop()
    popup_window = Popup(title = "ADD EMAIL COMPLETED", content = show, size_hint = (0.9, 0.2))
    popup_window.open()


# Add Panel Fail PopUp
class AddPanelFailPop(FloatLayout):
    pass

def show_AddPanelFailPop():
    show = AddPanelFailPop()
    popup_window = Popup(title = "ADD EMAIL ERROR", content = show, size_hint = (0.9, 0.2))
    popup_window.open()






# UpdatePanel Class
class UpdatePanel(Screen):
    def __init__(self, bucket=["","",""], back="MainPanel",**kwargs):
        self.bucket = bucket
        self.back = back
        super().__init__(**kwargs)
        
        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.9, 0.4
        self.info_grid.pos_hint = {"x": 0.05, "top": 0.67}

        self.past_name_label = Button(text = "Past Fullname:", font_size = 14)
        self.info_grid.add_widget(self.past_name_label)
        self.past_name_value = TextInput(text=self.bucket[0], multiline = False)
        self.info_grid.add_widget(self.past_name_value)
        self.past_email_label = Button(text = "Past Email Address:", font_size = 14)
        self.info_grid.add_widget(self.past_email_label)
        self.past_email_value = TextInput(text=self.bucket[1], multiline = False)
        self.info_grid.add_widget(self.past_email_value)
        self.past_category_label = Button(text = "Past Category:", font_size = 14)
        self.info_grid.add_widget(self.past_category_label)
        self.past_category_value = TextInput(text=self.bucket[2], multiline = False)
        self.info_grid.add_widget(self.past_category_value)

        self.new_name_label = Button(text = "New Fullname:", font_size = 14)
        self.info_grid.add_widget(self.new_name_label)
        self.new_name_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.new_name_value)
        self.new_email_label = Button(text = "New Email Address:", font_size = 14)
        self.info_grid.add_widget(self.new_email_label)
        self.new_email_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.new_email_value)
        self.new_category_label = Button(text = "New Category:", font_size = 14)
        self.info_grid.add_widget(self.new_category_label)
        self.new_category_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.new_category_value)

        self.add_widget(self.info_grid)
        self.submit_button = Button(text = "Update Email", font_size = 18, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.submit_button.size_hint = 0.4, 0.06
        self.submit_button.pos_hint = {"x":0.3,"top": 0.2}
        self.add_widget(self.submit_button)
        self.submit_button.bind(on_release = lambda x: self.update_mail_function())

    def update_mail_function(self):
        past_value_list = []
        past_value_list.append(self.past_name_value.text)
        past_value_list.append(self.past_email_value.text)
        past_value_list.append(self.past_category_value.text)
        new_value_list = []
        new_value_list.append(self.new_name_value.text)
        new_value_list.append(self.new_email_value.text)
        new_value_list.append(self.new_category_value.text)
        try:
            if ("" in new_value_list) or ("" in past_value_list):
                show_UpdatePanelFailPop()
            else:
                condition = database.update_mail(past_value_list, new_value_list)
                if condition == False:
                    show_UpdatePanelFailPop()
                else:
                    show_UpdatePanelSuccessPop()
        except:
            show_UpdatePanelFailPop()
        self.past_name_value.text = ""
        self.past_email_value.text = ""
        self.past_category_value.text = ""
        self.new_name_value.text = ""
        self.new_email_value.text = ""
        self.new_category_value.text = ""

    def go_to_website(self):
        go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "UpdatePanel":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = self.back


# Update Panel Success PopUp
class UpdatePanelSuccessPop(FloatLayout):
    pass

def show_UpdatePanelSuccessPop():
    show = UpdatePanelSuccessPop()
    popup_window = Popup(title = "UPDATE EMAIL COMPLETED", content = show, size_hint = (0.9, 0.2))
    popup_window.open()


# Update Panel Fail PopUp
class UpdatePanelFailPop(FloatLayout):
    pass

def show_UpdatePanelFailPop():
    show = UpdatePanelFailPop()
    popup_window = Popup(title = "UPDATE EMAIL ERROR", content = show, size_hint = (0.9, 0.2))
    popup_window.open()






# DeletePanel Class
class DeletePanel(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.9, 0.4
        self.info_grid.pos_hint = {"x": 0.05, "top": 0.67}

        self.name_label = Button(text = "Fullname:", font_size = 14)
        self.info_grid.add_widget(self.name_label)
        self.name_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.name_value)
        self.email_label = Button(text = "Email Address:", font_size = 14)
        self.info_grid.add_widget(self.email_label)
        self.email_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.email_value)
        self.category_label = Button(text = "Category:", font_size = 14)
        self.info_grid.add_widget(self.category_label)
        self.category_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.category_value)

        self.add_widget(self.info_grid)
        self.submit_button = Button(text = "Delete Email", font_size = 18, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.submit_button.size_hint = 0.4, 0.06
        self.submit_button.pos_hint = {"x":0.3,"top": 0.2}
        self.add_widget(self.submit_button)
        self.submit_button.bind(on_release = lambda x: self.delete_mail_function())

    def delete_mail_function(self):
        value_list = []
        value_list.append(self.name_value.text)
        value_list.append(self.email_value.text)
        value_list.append(self.category_value.text)
        try:
            if ("" in value_list):
                show_DeletePanelFailPop()
            else:
                condition = database.delete_mail(value_list)
                print(condition)
                if condition == False:
                    show_DeletePanelFailPop()
                else:
                    show_DeletePanelSuccessPop()
        except:
            show_DeletePanelFailPop()
        self.name_value.text = ""
        self.email_value.text = ""
        self.category_value.text = ""

    def go_to_website(self):
        go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "DeletePanel":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "MainPanel"


# Delete Panel Success PopUp
class DeletePanelSuccessPop(FloatLayout):
    pass

def show_DeletePanelSuccessPop():
    show = DeletePanelSuccessPop()
    popup_window = Popup(title = "DELETE EMAIL COMPLETED", content = show, size_hint = (0.9, 0.2))
    popup_window.open()


# Delete Panel Fail PopUp
class DeletePanelFailPop(FloatLayout):
    pass

def show_DeletePanelFailPop():
    show = DeletePanelFailPop()
    popup_window = Popup(title = "DELETE EMAIL ERROR", content = show, size_hint = (0.9, 0.2))
    popup_window.open()







# SendPanel Class
class SendPanel(Screen):
    def __init__(self, to = "", back = "MainPanel",**kwargs):
        self.to = to
        self.back = back
        super().__init__(**kwargs)

        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        self.info_grid.size_hint = 0.9, 0.6
        self.info_grid.pos_hint = {"x": 0.05, "top": 0.8}

        self.info_grid2 = GridLayout()
        self.info_grid2.cols = 2
        self.to_label = Button(text = "To:", font_size = 14)
        self.info_grid2.add_widget(self.to_label)
        self.to_value = TextInput(text=self.to, multiline = False)
        self.info_grid2.add_widget(self.to_value)
        self.subject_label = Button(text = "Subject:", font_size = 14)
        self.info_grid2.add_widget(self.subject_label)
        self.subject_value = TextInput(multiline = False)
        self.info_grid2.add_widget(self.subject_value)
        self.attachment_path_label = Button(text = "Attachment Path:", font_size = 14)
        self.info_grid2.add_widget(self.attachment_path_label)
        self.attachment_path_value = TextInput(multiline = False)
        self.info_grid2.add_widget(self.attachment_path_value)
        self.attachment_type_label = Button(text = "Attachment Type:", font_size = 14)
        self.info_grid2.add_widget(self.attachment_type_label)
        self.attachment_type_value = TextInput(multiline = False)
        self.info_grid2.add_widget(self.attachment_type_value)
        self.info_grid.add_widget(self.info_grid2)

        self.body_value = TextInput(multiline = True)
        self.info_grid.add_widget(self.body_value)

        self.add_widget(self.info_grid)
        self.submit_button = Button(text = "Send Email", font_size = 18, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.submit_button.size_hint = 0.4, 0.06
        self.submit_button.pos_hint = {"x":0.3,"top": 0.15}
        self.add_widget(self.submit_button)
        self.submit_button.bind(on_release = lambda x: self.send_mail_function())

    def send_mail_function(self):
        to = self.to_value.text
        subject = self.subject_value.text
        body = self.body_value.text
        attachment_path = self.attachment_path_value.text
        attachment_type = self.attachment_type_value.text

        try:
            if attachment_path == "" and attachment_type == "":
                print(mail.send_email(to, subject, body))
            else:
                mail.send_email(to, subject, body, attachment_path=attachment_path, attachment_type=attachment_type)
            show_SendPanelSuccessPop()
        except:
            show_SendPanelFailPop()
        self.to_value.text = ""
        self.subject_value.text = ""
        self.body_value.text = ""
        self.attachment_path_value.text = ""
        self.attachment_type_value.text = ""

    def go_to_website(self):
        go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "SendPanel":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = self.back


# Send Panel Success PopUp
class SendPanelSuccessPop(FloatLayout):
    pass

def show_SendPanelSuccessPop():
    show = SendPanelSuccessPop()
    popup_window = Popup(title = "SEND EMAIL COMPLETED", content = show, size_hint = (0.9, 0.2))
    popup_window.open()


# Send Panel Fail PopUp
class SendPanelFailPop(FloatLayout):
    pass

def show_SendPanelFailPop():
    show = SendPanelFailPop()
    popup_window = Popup(title = "SEND EMAIL ERROR", content = show, size_hint = (0.9, 0.2))
    popup_window.open()




# Search Panel class
class SearchPanel(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.9, 0.35
        self.info_grid.pos_hint = {"x": 0.05, "top": 0.615}

        self.key_label = Button(text = "Search Key:", font_size = 14)
        self.info_grid.add_widget(self.key_label)
        self.key_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.key_value)
        self.by_label = Button(text = "Search By:", font_size = 14)
        self.info_grid.add_widget(self.by_label)
        self.by_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.by_value)
        self.type_label = Button(text = "Search Type:", font_size = 14)
        self.info_grid.add_widget(self.type_label)
        self.type_value = TextInput(multiline = False)
        self.info_grid.add_widget(self.type_value)
        self.add_widget(self.info_grid)

        self.submit_button = Button(text = "Search Mail", font_size = 18, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.submit_button.size_hint = 0.4, 0.06
        self.submit_button.pos_hint = {"x":0.3,"top": 0.2}
        self.add_widget(self.submit_button)
        self.submit_button.bind(on_release = lambda x: self.search_mail_function())

    def search_mail_function(self):
        search_key = self.key_value.text
        search_by = self.by_value.text
        if search_by == "name":
            action = self.type_value.text
            try:
                info = database.search_mail(search_key,search_by=search_by,action=action)
                sm.add_widget(MailDisplayer(info, name="MailDisplayer"))
                sm.transition = SlideTransition(direction = "left")
                sm.current = "MailDisplayer"
            except:
                show_SearchPanelPop()
            self.type_value.text = ""
        else:
            try:
                info = database.search_mail(search_key,search_by=search_by)
                sm.add_widget(MailDisplayer(info, name="MailDisplayer"))
                sm.transition = SlideTransition(direction = "left")
                sm.current = "MailDisplayer"
            except:
                show_SearchPanelPop()
        self.key_value.text = ""
        self.by_value.text = ""


    def go_to_website(self):
        go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "SearchPanel":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "MainPanel"


# Search Panel PopUp
class SearchPanelPop(FloatLayout):
    pass

def show_SearchPanelPop():
    show = SearchPanelPop()
    popup_window = Popup(title = "SEARCH MAIL ERROR", content = show, size_hint = (0.9, 0.2))
    popup_window.open()



# Mail Displayer Class
class MailDisplayer(Screen):
    def __init__(self, info, **kwargs):
        super().__init__(**kwargs)
        self.info = info

        if len(self.info) == 0:
            self.no_label = Label(text = "THERE ISN'T ANY MAIL", color = (0/255, 153/255, 204/255, 1), font_size = 18)
            self.no_label.pos_hint = { "top": 1.01}
            self.add_widget(self.no_label)
            self.no_label_2 = Label(text = "WHICH CAN SATISFY YOUR QUERY", color = (0/255, 153/255, 204/255, 1), font_size = 18)
            self.no_label_2.pos_hint = { "top": 0.975}
            self.add_widget(self.no_label_2)

        self.headings = []
        for mail in self.info:
            self.headings.append([mail[1], None])
            
        self.scroller = ScrollView()
        self.scroller.pos_hint = {"x": 0.1, "top": 0.75}
        self.scroller.size_hint = (0.8, 0.63)
        
        self.info_grid = GridLayout()
        self.info_grid.cols = 1
        if len(self.headings) > 20:
            self.info_grid.size_hint = 1, 2
        elif len(self.headings) > 10:
            self.info_grid.size_hint = 1, 1.4
        elif len(self.headings) > 5: 
            self.info_grid.size_hint = 1, 0.8
        else:
            self.info_grid.size_hint = 1, 0.35
        
        i = -1
        for heading in self.headings:
            i += 1
            heading[1] = Button(text = heading[0], font_size = 15, on_release = lambda x, j=i: self.find_function(j))
            self.info_grid.add_widget(heading[1])
        self.scroller.add_widget(self.info_grid)

        self.footer = Image(
            source= 'resources/footer.png',
            size_hint = (0.98, 0.8),
            pos_hint= {"x": 0.01, "top": .135},
            size_hint_y=None, 
            height=100
        )
        self.add_widget(self.scroller)
        self.add_widget(self.footer)
        
    def find_function(self, i):
        sm.add_widget(MailInformation(self.info, name = "MailInformation"))
        MailInformation_screen = sm.get_screen('MailInformation')
        setattr(MailInformation_screen, "index", i)
        sm.transition = SlideTransition(direction = "left")
        sm.current = 'MailInformation'
        
    def go_to_website(self):
        mm.go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "MailDisplayer":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "SearchPanel"



class MailInformation(Screen):
    def __init__(self, mail_list, **kwargs):
        super().__init__(**kwargs)
        self.mail_list  = mail_list

    def on_pre_enter(self):
        mail = self.mail_list[self.index]
        self.mail = mail        

        self.info_grid = GridLayout()
        self.info_grid.cols = 2
        self.info_grid.size_hint = 0.9, 0.4
        self.info_grid.pos_hint = {"x": 0.05, "top": 0.67}

        self.name_label = Button(text = "Fullname:", font_size = 14, size_hint_x=None, width = 120)
        self.info_grid.add_widget(self.name_label)
        self.name_value = Label(text = mail[0], font_size = 14, color = (0,0,0,1))
        self.info_grid.add_widget(self.name_value)
        self.email_label = Button(text = "Email Address:", font_size = 14, size_hint_x=None, width = 120)
        self.info_grid.add_widget(self.email_label)
        self.email_value = Label(text = mail[1], font_size = 14, color = (0,0,0,1))
        self.info_grid.add_widget(self.email_value)
        self.category_label = Button(text = "Category:", font_size = 14, size_hint_x=None, width = 120)
        self.info_grid.add_widget(self.category_label)
        self.category_value = Label(text = mail[2], font_size = 14, color = (0,0,0,1))
        self.info_grid.add_widget(self.category_value)
        self.add_widget(self.info_grid)

        self.join_button = Button(text = "SEND", font_size = 16, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.join_button.size_hint = 0.25, 0.06
        self.join_button.pos_hint = {"x":0.075,"top": 0.2}
        self.add_widget(self.join_button)
        self.join_button.bind(on_release = lambda x: self.send_mail_function())

        self.join_button = Button(text = "UPDATE", font_size = 16, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.join_button.size_hint = 0.25, 0.06
        self.join_button.pos_hint = {"x":0.375,"top": 0.2}
        self.add_widget(self.join_button)
        self.join_button.bind(on_release = lambda x: self.update_mail_function())

        self.join_button = Button(text = "DELETE", font_size = 16, color = (1,1,1,1), background_color = (0/255, 153/255, 204/255, 1))
        self.join_button.size_hint = 0.25, 0.06
        self.join_button.pos_hint = {"x":0.675,"top": 0.2}
        self.add_widget(self.join_button)
        self.join_button.bind(on_release = lambda x: self.delete_mail_function())

    def send_mail_function(self):
        sm.add_widget(SendPanel(to=self.mail[1], back="MailInformation", name="SendPanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "SendPanel"
    
    def update_mail_function(self):
        sm.add_widget(UpdatePanel(bucket = self.mail, back="MailInformation", name="UpdatePanel"))
        sm.transition = SlideTransition(direction = "left")
        sm.current = "UpdatePanel"

    def delete_mail_function(self):
        value_list = self.mail
        try:
            if ("" in value_list):
                show_DeletePanelFailPop()
            else:
                condition = database.delete_mail(value_list)
                if condition == False:
                    show_DeletePanelFailPop()
                else:
                    show_DeletePanelSuccessPop()
        except:
            show_DeletePanelFailPop()

    def go_to_website(self):
        go_to_website()

    def go_back(self):
        for screen in sm.screens:
            if screen.name == "MailInformation":
                sm.screens.remove(screen)
        sm.transition = SlideTransition(direction = "right")
        sm.current = "MailDisplayer"






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