from kivy.app import App
from kivy.uix.screenmanager import (
    ScreenManager,
)
from kivy.lang import Builder

from startscreen import StartScreen
from homescreen import HomeScreen


class RootWidget(ScreenManager):
    Builder.load_file("root.kv")


class Test(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Here we store the username in the root.
        self.user = ""

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    Test().run()
