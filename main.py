import time

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from yeelight import Bulb


class MainPage(App):
    @staticmethod
    def run_s():
        bulb = Bulb("192.168.0.238")
        for x in range(10):
            bulb.turn_on(effect="sudden")
            time.sleep(0.3)
            bulb.turn_off()
            time.sleep(0.3)

    def execute_function(self, instance):
        self.run_s()

    def build(self):
        button_run = Button(text="run", on_release=self.execute_function)

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(button_run)

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    MainPage().run()
