import time

from yeelight import Bulb
import threading

from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class Screen1(Screen):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        self.add_widget(Button(text='Back', on_release=self.go_back, size_hint=(0.1, 0.1), pos_hint={'x': 0, 'top': 1}))
        self.add_widget(Button(text='Execute Function', on_release=self.execute_function, size_hint=(0.4, 0.2),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5}))

    def go_back(self, instance):
        self.manager.current = 'main'

    def execute_function(self, instance):
        threading.Thread(target=self.execute_function_thread).start()

    @staticmethod
    def execute_function_thread():
        bulb = Bulb("192.168.0.238")
        for x in range(10):
            bulb.turn_on(effect="sudden")
            time.sleep(0.3)
            bulb.turn_off()
            time.sleep(0.3)
