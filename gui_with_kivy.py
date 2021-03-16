import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text="Test")

if __name__ == "__main__":
    TestApp().run()