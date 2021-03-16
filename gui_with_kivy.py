import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class TestApp(App):
    def build(self):
        return Button(text="Test")

if __name__ == "__main__":
    TestApp().run()