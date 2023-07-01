import logging
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
# from yeelight import Bulb

log_file = os.path.join("lamp_control.log")
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class LampControl(BoxLayout):
    def __init__(self, **kwargs):
        super(LampControl, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50

        # self.bulb = Bulb("192.168.0.238")

        self.label = Label(text='Умная лампочка Yeelight', font_size='24sp', size_hint=(1, 0.4))
        self.add_widget(self.label)

        self.switch = Switch(active=False, size_hint=(1, 0.2))
        self.switch.bind(active=self.toggle_light)
        self.add_widget(self.switch)

    def toggle_light(self, instance, value):
        if value:
            # self.bulb.turn_on()
            logging.info("Лампочка включена")
        else:
            # self.bulb.turn_off()
            logging.info("Лампочка выключена")


class LampApp(App):
    def build(self):
        return LampControl()


if __name__ == '__main__':
    LampApp().run()
