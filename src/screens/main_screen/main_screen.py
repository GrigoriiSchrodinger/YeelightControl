from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        button1 = Button(text='Lamps', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        button1.bind(on_release=self.open_lamps_screen)

        button2 = Button(text='Scenario', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        button2.bind(on_release=self.open_scenario_screen)

        button3 = Button(text='Music', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        button3.bind(on_release=self.open_music_screen)

        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)

    def open_lamps_screen(self, instance):
        self.manager.current = 'lamps'

    def open_scenario_screen(self, instance):
        self.manager.current = 'scenario'

    def open_music_screen(self, instance):
        self.manager.current = 'music'

