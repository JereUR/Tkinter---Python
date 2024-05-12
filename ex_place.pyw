from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title('Place example')
window.geometry('400x200')


def fnAdd():
    x1 = n1.get()
    x2 = n2.get()
    r = float(x1)+float(x2)
    txt.config(text=r)


lbl1 = Label(window, text='First number', bg='yellow')
lbl1.place(relx=0.03, rely=0.03, relwidth=0.25, relheight=0.15)
n1 = Entry(window, bg='pink')
n1.place(relx=0.3, rely=0.03, relwidth=0.25, relheight=0.15)

lbl2 = Label(window, text='Second number', bg='yellow')
lbl2.place(x=10, y=50, width=100, height=30)
n2 = Entry(window, bg='pink')
n2.place(x=120, y=50, width=100, height=30)

btn1 = Button(window, text='Add', command=fnAdd)
btn1.place(x=230, y=50, width=80, height=30)

lbl3 = Label(window, text='Result', bg='yellow')
lbl3.place(x=10, y=120, width=100, height=30)
txt = Label(window, bg='pink')
txt.place(x=120, y=120, width=100, height=30)

window.mainloop()
