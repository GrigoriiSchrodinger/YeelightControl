import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from src.style.button_style import StyledButton


class AddingScreen(Screen):
    def __init__(self, **kwargs):
        super(AddingScreen, self).__init__(**kwargs)

        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        back_button = StyledButton(text='Back', on_release=self.go_back)
        top_bar.add_widget(back_button)

        content_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.name_input = TextInput(multiline=False, hint_text='Enter name')
        content_layout.add_widget(self.name_input)

        self.ip_input = TextInput(multiline=False, hint_text='Enter IP')
        content_layout.add_widget(self.ip_input)

        save_button = StyledButton(text='Save', on_release=self.save_lamps)
        content_layout.add_widget(save_button)

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(top_bar)
        main_layout.add_widget(content_layout)

        self.add_widget(main_layout)

    def go_back(self, instance):
        self.manager.current = 'lamps'

    def save_lamps(self, instance):
        url = 'http://10.0.0.3:9000'

        data = {'ip': self.ip_input.text, 'name': self.name_input.text}
        requests.post(url, data=data)
        self.manager.current = 'lamps'
