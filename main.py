from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from yeelight import Bulb


class LampControl(BoxLayout):
    def __init__(self, **kwargs):
        super(LampControl, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50

        self.bulb = Bulb("192.168.0.238")

        self.label = Label(text='Умная лампочка Yeelight', font_size='24sp', size_hint=(1, 0.4))
        self.add_widget(self.label)

        self.switch = Switch(active=False, size_hint=(1, 0.2))
        self.switch.bind(active=self.toggle_light)
        self.add_widget(self.switch)

    def toggle_light(self, instance, value):
        if value:
            self.bulb.turn_on()
        else:
            self.bulb.turn_off()


class LampApp(App):
    def build(self):
        return LampControl()


if __name__ == '__main__':
    LampApp().run()