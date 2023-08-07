from graphics import Point, Line


class Cell:
    def __init__(self, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        """
        Square:
        Top Left:       x1, y1
        Top Right:      x2, y1
        Bottom Left:    x1, y2
        Bottom Right:   x2, y2
        """
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            p1 = Point(x1, y1)
            p2 = Point(x1, y2)
            left_wall = Line(p1, p2)
            self._win.draw_line(left_wall)
        if self.has_right_wall:
            p1 = Point(x2, y1)
            p2 = Point(x2, y2)
            right_wall = Line(p1, p2)
            self._win.draw_line(right_wall)
        if self.has_top_wall:
            p1 = Point(x1, y1)
            p2 = Point(x2, y1)
            top_wall = Line(p1, p2)
            self._win.draw_line(top_wall)
        if self.has_bottom_wall:
            p1 = Point(x1, y2)
            p2 = Point(x2, y2)
            bottom_wall = Line(p1, p2)
            self._win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        x_self = ((self._x2 - self._x1) / 2) + self._x1
        y_self = ((self._y2 - self._y1) / 2) + self._y1
        x_remote = ((to_cell._x2 - to_cell._x1) / 2) + to_cell._x1
        y_remote = ((to_cell._y2 - to_cell._y1) / 2) + to_cell._y1

        center_self = Point(x_self, y_self)
        center_remote = Point(x_remote, y_remote)
        the_move = Line(center_self, center_remote)
        if undo:
            self._win.draw_line(the_move, "gray")
        else:
            self._win.draw_line(the_move, "red")
