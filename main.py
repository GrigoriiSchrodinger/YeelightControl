from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.screens.lamps_screen.lamps_screen import LampsScreen
from src.screens.main_screen.main_screen import MainScreen
from src.screens.music_screen.music_screen import MusicScreen
from src.screens.scenario_screen.scenario_screen import ScenarioScreen


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))

        sm.add_widget(LampsScreen(name='lamps'))
        sm.add_widget(ScenarioScreen(name='scenario'))
        sm.add_widget(MusicScreen(name='music'))

        return sm


if __name__ == '__main__':
    MyApp().run()