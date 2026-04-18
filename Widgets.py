from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.uix.widget import Widget


class RectangleWidget(Widget):
    def __init__(self, bg_color=(0.2, 0.6, 1, 1), **kwargs):
        super(RectangleWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(bg_color[0], bg_color[1], bg_color[2], bg_color[3])
            Rectangle(pos=self.pos, size=self.size)


class EllipseWidget(Widget):
    def __init__(self, bg_color=(0.2, 0.6, 1, 1), **kwargs):
        super(EllipseWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(bg_color[0], bg_color[1], bg_color[2], bg_color[3])
            Ellipse(pos=self.pos, size=self.size)


class LineWidget(Widget):
    def __init__(self, **kwargs):
        super(LineWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(self.bg_color[0], self.bg_color[1], self.bg_color[2], self.bg_color[3])
            self.line = Line(points=self.points, width=self.width, joint=self.joint, cap=self.cap)