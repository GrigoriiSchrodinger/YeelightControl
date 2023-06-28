from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.screens.lamps_screen.lamps_screen import Screen1
from src.screens.main_screen.main_screen import MainScreen
from src.screens.music_screen.music_screen import Screen3
from src.screens.scenario_screen.scenario_screen import Screen2


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