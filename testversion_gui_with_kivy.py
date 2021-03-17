"""
Diese Datei dient zur Übung mit kivy
Verwendete Tools:
- kivy
- time
Autor:
- data032547

"""
#Importieren der benötigten Libs
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from time import sleep 

#Standart App Code
class StandartApp(App):
    def build(self):
        return Button(text="Dies ist ein Standartfenster")

#Loginfeld Code
class Login(Widget):
    pass
class TestApp(App):
    def build(self):
        return Login()

#führt x-Objekt bei Test aus
if __name__ == "__main__":
    StandartApp().run()