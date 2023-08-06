from graphics import Window, Point, Line, Cell


def main():
    win = Window(800, 600)

    # p1 = Point(0, 0)
    # p2 = Point(800, 600)
    # l1 = Line(p1, p2)
    # win.draw_line(l1, "black")

    c1 = Cell(win, Point(50, 50), Point(100, 100))
    c1.draw()
    c2 = Cell(win, Point(150, 150), Point(200, 200))
    c2.has_bottom_wall = False
    c2.draw()
    c3 = Cell(win, Point(250, 250), Point(300, 300))
    c3.has_right_wall = False
    c3.draw()
    c4 = Cell(win, Point(350, 350), Point(400, 400))
    c4.has_top_wall = False
    c4.draw()
    win.wait_for_close()


main()
