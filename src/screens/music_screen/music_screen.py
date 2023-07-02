from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class MusicScreen(Screen):
    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)
        self.add_widget(Button(text='Back', on_release=self.go_back, size_hint=(0.2, 0.1), pos_hint={'x': 0, 'top': 1}))

    def go_back(self, instance):
        self.manager.current = 'main'
