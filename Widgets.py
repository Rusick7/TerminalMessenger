from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class RectangleWidget(Widget):
    def __init__(self, bg_color=(0.2, 0.6, 1, 1), **kwargs):
        super(RectangleWidget, self).__init__(**kwargs)

        with self.canvas:
            self.bg_color = bg_color
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size