"""
Diese Datei ist die Hauptdatei zur Ausführung des One_Sentences_Game
Verwendete Tools:
- kivy
- kivymd

Autor:
- data032547

"""
# Importieren der benötigten Tools
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from kivymd.app import MDApp

# Laden der entsprechenden .kv Datei
Builder.load_file('layout.kv')

class MAIN_LAYOUT(Widget):
    pass

class Main_App(MDApp):
    def build(self):
        return MAIN_LAYOUT()

#führt x-Objekt bei Test aus
if __name__ == "__main__":
    Main_App().run()
