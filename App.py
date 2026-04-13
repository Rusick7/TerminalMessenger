from kivy.config import Config
window_size=(800,600)
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', window_size[0])
Config.set('graphics', 'height', window_size[1])

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.codeinput import CodeInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.CW = (.10,.13,.15,1)
        self.CTI = self.CW #(.24,.24,.24,1)
        Window.clearcolor = self.CW

    def btn_press(self, instance):
        print("btn_press")

    def build(self):
        list_hor_widgets:list = [
            Button(
                text="Hello World!",
                font_size=30,
                on_press=self.btn_press,
                background_color=(.13,.16,.18,1),
                background_normal='',
                size_hint=(1/3,.2),
                pos=(0,0)
            ),
            Button(
                text="Hello",
                font_size=30,
                on_press=self.btn_press,
                size_hint=(1/3,.2),
                pos=(window_size[0]/3,0)
            ),
            Button(
                text="World!",
                font_size=30,
                on_press=self.btn_press,
                size_hint=(1/3,.2),
                pos=(window_size[0]/3*2,0)
            )
        ]

        flh = FloatLayout(size = (200, 200))
        for hor in list_hor_widgets:
            flh.add_widget(hor)

        list_ver_widgets:list = [
            CodeInput(font_size=12,
                      size_hint=(1,.8),
                      pos=(0,window_size[1]*.2),
                      background_color=self.CTI,
                      ),
            flh
        ]

        flv = FloatLayout(size = (200, 200))
        for vert in list_ver_widgets:
            flv.add_widget(vert)
        return flv

    def on_start(self):
        pass

    def on_stop(self):
        pass

if __name__ == "__main__":
    MyApp().run()