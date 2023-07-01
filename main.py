import json
import logging
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class LampControl(BoxLayout):
    def __init__(self, **kwargs):
        super(LampControl, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50

        self.label = Label(text='Умная лампочка Yeelight', font_size='24sp', size_hint=(1, 0.4))
        self.add_widget(self.label)

        self.switch = Switch(active=False, size_hint=(1, 0.2))
        self.switch.bind(active=self.toggle_light)
        self.add_widget(self.switch)

    @staticmethod
    def toggle_light(instance, value):
        if value:
            url = 'http://10.0.0.3:9000'
            data = {'key': 'value'}

            headers = {'Content-Type': 'application/json'}
            requests.get(url, headers=headers, data=json.dumps(data))
        else:
            logging.info("Лампочка выключена")


class LampApp(App):
    def build(self):
        return LampControl()


if __name__ == '__main__':
    LampApp().run()
