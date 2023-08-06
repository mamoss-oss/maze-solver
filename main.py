from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(800, 600)
    l1 = Line(p1, p2)
    win.draw_line(l1, "black")
    win.wait_for_close()


main()
