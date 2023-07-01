# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager
#
# from src.screens.lamps_screen.lamps_screen import Screen1
# from src.screens.main_screen.main_screen import MainScreen
# from src.screens.music_screen.music_screen import Screen3
# from src.screens.scenario_screen.scenario_screen import Screen2
#
#
# class MyApp(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(MainScreen(name='main'))
#         sm.add_widget(Screen1(name='screen1'))
#         sm.add_widget(Screen2(name='screen2'))
#         sm.add_widget(Screen3(name='screen3'))
#
#         return sm
#
#
# if __name__ == '__main__':
#     MyApp().run()

'''
Mesh test
=========

This demonstrates the use of a mesh mode to distort an image. You should see
a line of buttons across the bottom of a canvas. Pressing them displays
the mesh, a small circle of points, with different mesh.mode settings.
'''
# import threading
# import time

from kivy.app import App
# from kivy.clock import Clock
from kivy.uix.button import Button
# from yeelight import Bulb


class SimpleApp(App):
    def build(self):
        btn1 = Button(text='Hello world 1')
        btn1.bind(on_press=self.callback)
        btn2 = Button(text='Hello world 2')
        btn2.bind(on_press=self.callback)

    @staticmethod
    def callback(instance):
        print('The button <%s> is being pressed' % instance.text)

    # def execute_function(self, instance):
    #     Clock.schedule_once(lambda dt: self.execute_function_thread(), 0)
    #
    # def execute_function_thread(self):
    #     threading.Thread(target=self.execute_function_thread_helper).start()
    #
    # @staticmethod
    # def execute_function_thread_helper():
    #     bulb = Bulb("192.168.0.238")
    #     for x in range(10):
    #         bulb.turn_on(effect="sudden")
    #         time.sleep(0.3)
    #         bulb.turn_off()
    #         time.sleep(0.3)


if __name__ == "__main__":
    SimpleApp().run()
