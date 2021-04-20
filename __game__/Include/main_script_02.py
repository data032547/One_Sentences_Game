"""
Diese Datei ist die Hauptdatei zur Ausführung des One_Sentences_Game
Verwendete Tools:
- kivy
- time
- kivymd
- ast
- os
- sys
- pathlib
- u.a. 

Autor:
- data032547

"""
# Importieren der benötigten Tools
import ast
import os
import sys
from pathlib import Path

from kivy.core.window import Window
from kivy.factory import Factory  # NOQA: F401
from kivy.lang import Builder
from kivy.loader import Loader
from libs.baseclass.dialog_change_theme import (
    KitchenSinkDialogChangeTheme,
    KitchenSinkUsageCode,
)
from libs.baseclass.list_items import (  # NOQA: F401
    KitchenSinkOneLineLeftIconItem,
)

from kivymd import images_path
from kivymd.app import MDApp



class MyApp(App):
    def build(self):
        return MyGridLayout()

#führt x-Objekt bei Test aus
if __name__ == "__main__":
    MyApp().run()
