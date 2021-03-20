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
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from time import sleep 

#Standart App Code
class StandartApp(App):
    def build(self):
        return Button(text="Dies ist ein Standartfenster")

# Vorbereitung eines Modules für's Spiel
class MyGridLayout(GridLayout):
    def __init__(self,anzeige="None",letzter_satz="None"):
        self.letzter_satz = letzter_satz
        #Constructor Call
        super(MyGridLayout, self).__init__()

        self.fenster_laden()

    def fenster_laden(self):
        # setzte Säulen
        self.cols = 2
        # setzte letzen Satz Label
        self.add_widget(Label(text=self.letzter_satz, font_size = 32))
        # setzte Input
        text = TextInput(multiline=False)
        self.add_widget(text)
        # setzte Button
        absenden = Button(text="absenden", font_size = 32)
        self.add_widget(absenden)

class Test(App):
    def build(self):
        return MyGridLayout()

#führt x-Objekt bei Test aus
if __name__ == "__main__":
    Test().run()