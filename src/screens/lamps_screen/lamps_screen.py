import json
import threading
import requests

from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class LampsScreen(Screen):
    def __init__(self, **kwargs):
        super(LampsScreen, self).__init__(**kwargs)
        self.add_widget(Button(text='Back', on_release=self.go_back, size_hint=(0.1, 0.1), pos_hint={'x': 0, 'top': 1}))
        self.add_widget(Button(text='Execute Function', on_release=self.execute_function, size_hint=(0.4, 0.2),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5}))

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
