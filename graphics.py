from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, heigth: int) -> None:
        self.__root = Tk()  # Root widget
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=heigth, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Window closed...")

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line, fill_color: str = "black") -> None:
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, win: Window, p1: Point, p2: Point) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self._win = win

    def draw(self):
        """
        Square:
        Top Left:       x1, y1
        Top Right:      x2, y1
        Bottom Left:    x1, y2
        Bottom Right:   x2, y2
        """
        if self.has_left_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_wall = Line(p1, p2)
            self._win.draw_line(left_wall)
        if self.has_right_wall:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            right_wall = Line(p1, p2)
            self._win.draw_line(right_wall)
        if self.has_top_wall:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            top_wall = Line(p1, p2)
            self._win.draw_line(top_wall)
        if self.has_bottom_wall:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            bottom_wall = Line(p1, p2)
            self._win.draw_line(bottom_wall)
