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

