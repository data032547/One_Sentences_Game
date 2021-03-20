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
    def __init__(self,liste=[]):
        self.liste = liste

        #Constructor Call
        super(MyGridLayout, self).__init__()

        self.fenster_laden()

    def fenster_laden(self):
        # setzte Säulen
        self.cols = 1

        # setzte letzen Satz Label
        self.letzter_satz = Label(text="None", font_size = 32)
        self.add_widget(self.letzter_satz)

        # setzte Input
        self.satz = TextInput(multiline=True,text="Satz hier eingeben...",font_size=32)
        self.add_widget(self.satz)

        # setzte Button absenden
        absenden = Button(text="absenden", font_size = 32)
        absenden.bind(on_press=self.next)
        self.add_widget(absenden)

        # setzte Button Spiel beenden
        beenden = Button(text="Spiel beenden", font_size = 22)
        beenden.bind(on_press=self.ende)
        self.add_widget(beenden)


    def next(self,instance):
        self.liste = self.liste + self.satz.text

        #clear
        self.letzter_satz.text = self.satz.text
        self.satz.text = "Satz hier eingeben..."

    def ende(self):
        print(self.liste)

class Test(App):
    def build(self):
        return MyGridLayout()

#führt x-Objekt bei Test aus
if __name__ == "__main__":
    Test().run()