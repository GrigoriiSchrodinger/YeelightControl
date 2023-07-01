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
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# from yeelight import Bulb


# class SimpleApp(App):
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


from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial


class StressCanvasApp(App):

    def add_rects(self, label, wid, count, *largs):
        label.text = str(int(label.text) + count)
        with wid.canvas:
            for x in range(count):
                Color(r(), 1, 1, mode='hsv')
                Rectangle(pos=(r() * wid.width + wid.x,
                               r() * wid.height + wid.y), size=(20, 20))

    def double_rects(self, label, wid, *largs):
        count = int(label.text)
        self.add_rects(label, wid, count, *largs)

    def reset_rects(self, label, wid, *largs):
        label.text = '0'
        wid.canvas.clear()

    def build(self):
        wid = Widget()

        label = Label(text='0')

        btn_add100 = Button(text='+ 100 rects',
                            on_press=partial(self.add_rects, label, wid, 100))

        btn_add500 = Button(text='+ 500 rects',
                            on_press=partial(self.add_rects, label, wid, 500))

        btn_double = Button(text='x 2',
                            on_press=partial(self.double_rects, label, wid))

        btn_reset = Button(text='Reset',
                           on_press=partial(self.reset_rects, label, wid))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add100)
        layout.add_widget(btn_add500)
        layout.add_widget(btn_double)
        layout.add_widget(btn_reset)
        layout.add_widget(label)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    StressCanvasApp().run()
