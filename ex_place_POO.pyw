from tkinter import Tk, Label, Button, Entry, Frame


class FrAdd(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def fnAdd(self):
        x1 = self.n1.get()
        x2 = self.n2.get()
        r = float(x1)+float(x2)
        self.txt.config(text=r)

    def create_widgets(self):
        self.lbl1 = Label(self, text='First number', bg='yellow')
        self.lbl1.place(x=10, y=10, width=100, height=30)
        self.n1 = Entry(self, bg='pink')
        self.n1.place(x=120, y=10, width=100, height=30)

        self.lbl2 = Label(self, text='Second number', bg='yellow')
        self.lbl2.place(x=10, y=50, width=100, height=30)
        self.n2 = Entry(self, bg='pink')
        self.n2.place(x=120, y=50, width=100, height=30)

        self.btn1 = Button(self, text='Add', command=self.fnAdd)
        self.btn1.place(x=230, y=50, width=80, height=30)

        self.lbl3 = Label(self, text='Result', bg='yellow')
        self.lbl3.place(x=10, y=120, width=100, height=30)
        self.txt = Label(self, bg='pink')
        self.txt.place(x=120, y=120, width=100, height=30)


root = Tk()
root.wm_title('Add numbers')
app = FrAdd(root)
app.mainloop()
