from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class RectangleWidget(Widget):
    def __init__(self, bg_color=(0.2, 0.6, 1, 1), **kwargs):
        super(RectangleWidget, self).__init__(**kwargs)

        with self.canvas:
            self.color = Color(*bg_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.rect.pos = self.pos
        self.rect.size = self.size



class EllipseWidget(Widget):
    def __init__(self, bg_color=(0.2, 0.6, 1, 1), **kwargs):
        super(EllipseWidget, self).__init__(**kwargs)

        with self.canvas:
            self.color = Color(*bg_color)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)

        self.ellipse.pos = self.pos
        self.ellipse.size = self.size


class LineWidget(BoxLayout):
    def __init__(self, bg_color=(1,1,1,1), width=1, padding=0, points=None, joint='round', cap='round', **kwargs):
        super().__init__(**kwargs)
        if points is None: 
            points = []
        self.padding = padding
        self.line_width = width

        with self.canvas.before:
            Color(*bg_color)
            self.line = Line(points=points, width=width,
                             joint=joint, cap=cap)

        self.line.points = points
        self.line.width = width





def fit_points_to_window(points, window_size, width, padding):
    fitted_points = []
    for x, y in points:
        fitted_points.extend([
            wrap_coordinate(x, window_size[0], width, padding),
            wrap_coordinate(y, window_size[1], width, padding)
        ])
    return fitted_points

def wrap_coordinate(point, max_value, width, padding):
    if point > max_value - padding:
        return point - padding*2 - width/2
    elif point < padding:
        return point + padding*2 + width/2
    return point