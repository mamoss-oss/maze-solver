from graphics import Window, Point, Line, Cell


def main():
    win = Window(800, 600)

    # p1 = Point(0, 0)
    # p2 = Point(800, 600)
    # l1 = Line(p1, p2)
    # win.draw_line(l1, "black")

    c1 = Cell(win)
    c1.draw(50, 50, 100, 100)
    c2 = Cell(win)
    c2.has_bottom_wall = False
    c2.draw(150, 150, 200, 200)
    c3 = Cell(win)
    c3.has_right_wall = False
    c3.draw(250, 250, 300, 300)
    c4 = Cell(win)
    c4.has_top_wall = False
    c4.draw(350, 350, 400, 400)
    win.wait_for_close()


main()
