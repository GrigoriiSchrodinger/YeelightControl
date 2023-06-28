from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from src.screens.lamps_screen.lamps_screen import Screen1
from src.screens.music_screen.music_screen import Screen3
from src.screens.scenario_screen.scenario_screen import Screen2


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        button1 = Button(text='Screen 1', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        button1.bind(on_release=self.go_to_screen1)

        button2 = Button(text='Screen 2', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button2.bind(on_release=self.go_to_screen2)

        button3 = Button(text='Screen 3', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        button3.bind(on_release=self.go_to_screen3)

        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)

    def go_to_screen1(self, instance):
        self.manager.current = 'screen1'

    def go_to_screen2(self, instance):
        self.manager.current = 'screen2'

    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))

        return sm


if __name__ == '__main__':
    MyApp().run()
