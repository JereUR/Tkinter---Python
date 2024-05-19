from tkinter import Tk
from mainFrame import MainFrame


def main():
    root = Tk()
    root.wm_title('Fracciones Mixtas')
    app = MainFrame(root)
    app.mainloop()


if __name__ == '__main__':
    main()
