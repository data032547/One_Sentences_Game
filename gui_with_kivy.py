from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from time import sleep 

class Login(Widget):
    pass
class TestApp(App):
    def build(self):
        return Login()

if __name__ == "__main__":
    TestApp().run()