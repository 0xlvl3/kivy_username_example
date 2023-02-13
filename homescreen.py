from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class HomeScreen(Screen):
    pass


kv_homescreen = """
<HomeScreen>
    FloatLayout:
        Label:
            id: current_user
            text: ""
        Button:
            text: "exit test"
            size_hint: 0.4, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            on_press: exit()
"""

Builder.load_string(kv_homescreen)
