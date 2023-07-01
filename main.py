from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from yeelight import Bulb


class MainPage(App):
    @staticmethod
    def run_s():
        times = 0
        print(times + 33)
        # bulb = Bulb("192.168.0.238")
        # bulb.turn_on(effect="sudden")

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
