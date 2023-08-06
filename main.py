from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, heigth):
        self.__root = Tk()  # Root widget
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=heigth, bg="white")
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False


def main():
    win = Window(600, 600)
    win.wait_for_close()


main()
