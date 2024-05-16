from tkinter import Tk, Label, Button, Entry, Frame


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def fCalcular(self):
        pass

    def create_widgets(self):
        """ Fraccion 1 """
        fFrac1 = Frame(self, width=100, height=60)
        fFrac1.place(x=30, y=20)

        fx1 = Frame(fFrac1, width=42, height=27)
        fx1.grid(row=0, column=0, rowspan=2)

        Label(fx1, text='Ent').pack(side='left')

        self.txt1E = Entry(fx1, width=4)
        self.txt1E.pack(side='right')

        self.txt1N = Entry(fFrac1, width=4)
        self.txt1D = Entry(fFrac1, width=4)

        self.txt1N.grid(row=0, column=1)
        self.txt1D.grid(row=1, column=1)

        Label(fFrac1, text='Num').grid(row=0, column=2)
        Label(fFrac1, text='Den').grid(row=1, column=2)

        """ Fraccion 2 """
        fFrac2 = Frame(self, width=100, height=60)
        fFrac2.place(x=180, y=20)

        fx2 = Frame(fFrac2, width=42, height=27)
        fx2.grid(row=0, column=0, rowspan=2)

        Label(fx2, text='Ent').pack(side='left')

        self.txt2E = Entry(fx2, width=4)
        self.txt2E.pack(side='right')

        self.txt2N = Entry(fFrac2, width=4)
        self.txt2D = Entry(fFrac2, width=4)

        self.txt2N.grid(row=0, column=1)
        self.txt2D.grid(row=1, column=1)

        Label(fFrac2, text='Num').grid(row=0, column=2)
        Label(fFrac2, text='Den').grid(row=1, column=2)

        Label(self, text='Fracción 1:').place(x=48, y=8)
        Label(self, text='Fracción 2:').place(x=198, y=8)

        Label(self, text='Operación:').place(x=30, y=90)
        Label(self, text='Resultado:').place(x=30, y=120)

        self.txtRes = Entry(self, width=15)
        self.txtRes.place(x=100, y=120)

        self.btnCalcular = Button(
            self, text='Calcular', command=self.fCalcular)
        self.btnCalcular.place(x=210, y=90)


root = Tk()
root.wm_title('Fracciones Mixtas')
app = MainFrame(root)
app.mainloop()
