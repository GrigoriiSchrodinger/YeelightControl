import threading

import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from src.style.button_style import StyledButton


class LampsScreen(Screen):
    def __init__(self, **kwargs):
        super(LampsScreen, self).__init__(**kwargs)

        self.content_layout = GridLayout(cols=2, spacing=10, padding=10)

        top_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        lower_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        back_button = StyledButton(text='Back', on_release=self.go_back)
        plus_button = StyledButton(text='+', on_release=self.go_adding)
        all_on = StyledButton(text='ON', on_release=self.all_on_thread)
        all_off = StyledButton(text='OFF', on_release=self.all_off_thread)

        top_bar.add_widget(back_button)
        top_bar.add_widget(plus_button)
        lower_bar.add_widget(all_on)
        lower_bar.add_widget(all_off)

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(top_bar)
        main_layout.add_widget(self.content_layout)
        main_layout.add_widget(lower_bar)

        self.add_widget(main_layout)

    def on_enter(self):
        self.refresh_screen()

    def refresh_screen(self):
        self.content_layout.clear_widgets()

        response = requests.get('http://10.0.0.3:9000/lamps').json()

        for item in response:
            button_layout = BoxLayout(orientation='vertical')

            button = StyledButton(
                text=f"{item[1]}",
                on_release=lambda instance, ip=item[0]: self.focus_lamp_thread(instance, ip),
                size_hint=(1, 1),
            )
            button_layout.add_widget(button)
            self.content_layout.add_widget(button_layout)

    def go_back(self, instance):
        self.manager.current = 'main'

    def go_adding(self, instance):
        self.manager.current = 'adding'

    # ------------------------------------------------------------------------------------------------------------------
    def focus_lamp_thread(self, instance, ip):
        threading.Thread(target=lambda: self.focus_lamp(ip)).start()

    @staticmethod
    def focus_lamp(ip):
        url = 'http://10.0.0.3:9000/focus'
        data = {'ip': ip}
        requests.post(url, data=data)

    # ------------------------------------------------------------------------------------------------------------------

    def all_on_thread(self, instance):
        threading.Thread(target=self.all_on).start()

    @staticmethod
    def all_on():
        url = 'http://10.0.0.3:9000/all'
        data = {'action': "on"}
        requests.post(url, data=data)

    # ------------------------------------------------------------------------------------------------------------------

    def all_off_thread(self, instance):
        threading.Thread(target=self.all_off).start()

    @staticmethod
    def all_off():
        url = 'http://10.0.0.3:9000/all'
        data = {'action': "off"}
        requests.post(url, data=data)
