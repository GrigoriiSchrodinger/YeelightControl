from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


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

