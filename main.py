from kivy import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.screens.main_screen.lamps_screen.adding_screen.adding_screen import AddingScreen
from src.screens.main_screen.lamps_screen.lamps_screen import LampsScreen
from src.screens.main_screen.main_screen import MainScreen
from src.screens.main_screen.scenario_screen.scenario_screen import ScenarioScreen

Config.set('graphics', 'maxfps', '120')


class MyApp(App):
    def build(self):
        root = ScreenManager()

        root.add_widget(MainScreen(name='main'))

        root.add_widget(LampsScreen(name='lamps'))
        root.add_widget(ScenarioScreen(name='scenario'))
        root.add_widget(AddingScreen(name='adding'))

        return root


if __name__ == '__main__':
    MyApp().run()
