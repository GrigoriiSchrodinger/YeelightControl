from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from src.style.button_style import StyledButton


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        button_bar = BoxLayout(orientation='vertical')
        button_lamps = StyledButton(text='Lamps')
        button_lamps.bind(on_release=self.open_lamps_screen)

        button_scenario = StyledButton(text='Scenario')
        button_scenario.bind(on_release=self.open_scenario_screen)

        button_bar.add_widget(button_lamps)
        button_bar.add_widget(button_scenario)

        self.add_widget(button_bar)

    def open_lamps_screen(self, instance):
        self.manager.current = 'lamps'

    def open_scenario_screen(self, instance):
        self.manager.current = 'scenario'
