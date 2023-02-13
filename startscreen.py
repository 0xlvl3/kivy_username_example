from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.app import App


class StartScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.username = ""  # Create a username variable.

    def go_to_home(self):
        # We then store the text input within the username field.
        self.username = self.manager.current_screen.ids.username.text

        # Then we get the user variable we created in our main.py, by using App.get_running_app.
        # Store the self.username input.
        App.get_running_app().user = self.username

        # We then get the homescreen and change the current_user Label text to the string below.
        self.manager.get_screen(
            "home_screen"
        ).ids.current_user.text = f"Welcome {self.username}!"

        # Switch to the home screen.
        self.manager.current = "home_screen"


kv_startscreen = """
<StartScreen>
    FloatLayout:
        Label:
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}          
            text: "Log in to go to home screen"
        TextInput:
            hint_text: "Username"
            id: username
            size_hint: 0.4, 0.07
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        TextInput:
            hint_text: "Password"
            size_hint: 0.4, 0.07
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        Button:
            text: "Log in!"
            size_hint: 0.4, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            on_press: root.go_to_home()
"""

Builder.load_string(kv_startscreen)
