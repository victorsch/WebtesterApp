from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, FadeTransition, Screen
from kivy.properties import StringProperty
from kivy.clock import Clock


class BaseWindow(Screen):

    def __init__(self, **kwargs):
        super(BaseWindow, self).__init__(**kwargs)

    def diagnostics(self):
        print("Hey it works!")

class HttpMethodDropDown(DropDown):
    def select(self, data):
        print("Dropdown was selected")


class DiagScreen(Screen):
    xstring = StringProperty("Diagnostics String!")

    def changestring(self):
        self.text = "Here's the new one"
        print(self.text)
        print("It works but we gotta update.")

class ScreenManagement(ScreenManager):
    pass


class WebtesterApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main_page = BaseWindow()
        screen = Screen(name="base")
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        self.diag_page = DiagScreen()
        screen = Screen(name="diag")
        screen.add_widget(self.diag_page)
        self.screen_manager.add_widget(screen)
        return  self.screen_manager



if __name__ == '__main__':
    webtester = WebtesterApp()
    webtester.run()
