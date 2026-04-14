
from Config import *
from Widgets import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.app import App


class MyApp(App):
    def __init__(self):
        super().__init__()
        # self.CW = (26/255,32/255,38/255,1)
        self.CW = (20/255,20/255,20/255,1)
        self.CTI = (.24,.24,.24,1)
        Window.clearcolor = self.CW

    @staticmethod
    def btn_press(instance):
        print("btn_press")

    @staticmethod
    def add_widget(layout: AnchorLayout|BoxLayout, widgets:list):
        for el in widgets:
            layout.add_widget(el)
        return layout

    # ---------------------------------- UP / TOP ---------------------------------

    def upper(self):
        # fl = FloatLayout()
        # fl.add_widget(RectangleWidget(pos=(0,window_size[1]-30)))
        # fl.add_widget(Label(text="User 2",font_size=16))

        widgets: list = [
            Image(
                source='./img/user2.png',
                size_hint_x=0.1,
            ),
            Label(
                text="User 2",
                font_size=16
            ),
            Image(
                source='./img/settings.png',
                size_hint_x=0.1,
            )
        ]

        return self.add_widget(BoxLayout(size_hint=[1, .04]), widgets)

    # ---------------------------------- CENTER ---------------------------------

    # def center(self):
    #     widgets: list = [
    #         Widget()
    #     ]
    #
    #     return self.add_widget(BoxLayout(), widgets)

    # ---------------------------------- DOWN / BOTTOM ---------------------------------

    def downer(self):
        widgets: list = [
            Button(
                text="Hello World!",
                font_size=12,
                size_hint_x=0.1,
                on_press=self.btn_press,
                background_color=(.13, .16, .18, 1),
                background_normal='',
            ),
            TextInput(
                font_size=12,
                background_color=self.CTI,
            ),
            Button(
                text="World!",
                font_size=12,
                size_hint_x=0.1,
                on_press=self.btn_press,
            )
        ]

        return self.add_widget(BoxLayout(size_hint=[1, .06]), widgets)

    # ---------------------------------- BODY ---------------------------------

    def body(self, upper, downer):
        widgets: list = [
            upper,
            Widget(), #center,
            downer,
        ]

        return self.add_widget(BoxLayout(orientation='vertical'), widgets)

    # =========================================================================

    def front(self, body):
        widgets: list = [
            Image(
                source='./img/icon.png',
                allow_stretch=True,
                keep_ratio=True,
                size_hint=(1,1),
            ),
            body
        ]

        return self.add_widget(FloatLayout(), widgets)


    def build(self):
        return self.front(self.body(
            upper=self.upper(),
            downer=self.downer()
        ))

    def on_start(self):
        pass

    def on_stop(self):
        pass

if __name__ == "__main__":
    MyApp().run()