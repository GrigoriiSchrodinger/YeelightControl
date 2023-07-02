import json
import threading

import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from src.style.button_style import StyledButton


class LampsScreen(Screen):
    def __init__(self, **kwargs):
        super(LampsScreen, self).__init__(**kwargs)

        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        back_button = StyledButton(text='Back', on_release=self.go_back)
        plus_button = StyledButton(text='+', on_release=self.go_back)

        top_bar.add_widget(back_button)
        top_bar.add_widget(plus_button)

        content_layout = GridLayout(cols=2, spacing=10, padding=10)

        for _ in range(13):
            button_layout = BoxLayout(orientation='vertical')

            button = StyledButton(
                text=f"{_}",
                on_release=self.execute_function,
                size_hint=(1, 1),
            )
            button_layout.add_widget(button)
            content_layout.add_widget(button_layout)

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(top_bar)
        main_layout.add_widget(content_layout)

        self.add_widget(main_layout)

    def go_back(self, instance):
        self.manager.current = 'main'

    def execute_function(self, instance):
        threading.Thread(target=self.execute_function_thread).start()

    @staticmethod
    def execute_function_thread():
        url = 'http://192.168.0.139:9000'
        data = {'key': 'value'}

        headers = {'Content-Type': 'application/json'}
        requests.get(url, headers=headers, data=json.dumps(data))
