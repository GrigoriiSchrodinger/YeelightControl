import threading

import requests
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from src.style.button_style import StyledButton
from src.utils.config import IP


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
        night = StyledButton(text='NIGHT', on_release=self.night_lamp_thread)

        top_bar.add_widget(back_button)
        top_bar.add_widget(plus_button)
        lower_bar.add_widget(all_on)
        lower_bar.add_widget(all_off)
        lower_bar.add_widget(night)

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(top_bar)
        main_layout.add_widget(self.content_layout)
        main_layout.add_widget(lower_bar)

        self.add_widget(main_layout)

    def on_enter(self):
        self.refresh_screen()

    def refresh_screen(self):
        self.content_layout.clear_widgets()

        response = requests.get(f'{IP}/lamps').json()

        for item in response:
            button_layout = BoxLayout(orientation='horizontal')

            button_focus = StyledButton(
                text=f"{item[1]}",
                on_release=lambda instance, ip=item[0]: self.focus_lamp_thread(instance, ip),
            )

            button_dead = StyledButton(
                text="dead",
                on_release=lambda instance, ip=item[0]: self.dead_lamp_thread(instance, ip),
            )

            if item[3] == 1:
                button_dead.background_color = (1, 0, 0, 1)

            button_layout.add_widget(button_focus)
            button_layout.add_widget(button_dead)

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
        url = f'{IP}/focus'
        data = {'ip': ip}
        requests.post(url, data=data)

        sound = SoundLoader.load('src/sound/switch-lamp-switch-clicking_fk4jxsnu.mp3')
        if sound:
            sound.play()

    # ------------------------------------------------------------------------------------------------------------------

    def all_on_thread(self, instance):
        threading.Thread(target=self.all_on).start()

    @staticmethod
    def all_on():
        url = f'{IP}/all'
        data = {'action': "on"}
        requests.post(url, data=data)

    # ------------------------------------------------------------------------------------------------------------------

    def all_off_thread(self, instance):
        threading.Thread(target=self.all_off).start()

    @staticmethod
    def all_off():
        url = f'{IP}/all'
        data = {'action': "off"}
        requests.post(url, data=data)

    # ------------------------------------------------------------------------------------------------------------------

    def dead_lamp_thread(self, instance, ip):
        threading.Thread(target=lambda: self.dead_lamp(ip)).start()

    @staticmethod
    def dead_lamp(ip):
        url = f'{IP}/dead'
        data = {'ip': ip}
        requests.post(url, data=data)

    # ------------------------------------------------------------------------------------------------------------------

    def night_lamp_thread(self, instance):
        threading.Thread(target=self.night_lamp).start()

    @staticmethod
    def night_lamp():
        url = f'{IP}/night'
        requests.get(url)
