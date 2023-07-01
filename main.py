import logging

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from yeelight import Bulb


class MainPage(App):
    logging.basicConfig(level=logging.DEBUG,
                        filename='app.log',
                        format='%(asctime)s [%(levelname)s]: %(message)s')

    @staticmethod
    def run_s():
        try:
            bulb = Bulb("192.168.0.238")
            bulb.turn_on(effect="sudden")
        except Exception as e:
            logging.exception("Произошла ошибка: %s", str(e))

    def execute_function(self, instance):
        self.run_s()

    def build(self):
        try:
            button_run = Button(text="run", on_release=self.execute_function)

            layout = BoxLayout(size_hint=(1, None), height=50)
            layout.add_widget(button_run)

            root = BoxLayout(orientation='vertical')
            root.add_widget(layout)

            return root
        except Exception as e:
            logging.exception("Произошла ошибка: %s", str(e))


if __name__ == '__main__':
    MainPage().run()
