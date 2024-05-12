from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title('Grid example')
window.geometry('400x300')


def fnAdd():
    x1 = n1.get()
    x2 = n2.get()
    r = float(x1)+float(x2)
    txt.config(text=r)


lbl1 = Label(window, text='First number', bg='yellow')
n1 = Entry(window, bg='pink')
lbl2 = Label(window, text='Second number', bg='yellow')
n2 = Entry(window, bg='pink')
btn1 = Button(window, text='Add', command=fnAdd)
lbl3 = Label(window, text='Result', bg='yellow')
txt = Label(window, bg='pink')

lbl1.grid(row=0, column=0, padx=6, pady=6, sticky='w', ipady=6)
n1.grid(row=0, column=1, padx=6, pady=6)
lbl2.grid(row=1, column=0, padx=6, pady=6, sticky='w', ipady=6)
n2.grid(row=1, column=1, padx=6, pady=6)
btn1.grid(row=1, column=2, padx=6, pady=6, ipadx=10, ipady=4)
lbl3.grid(row=2, column=0, padx=6, pady=6, sticky='w', ipady=6)
txt.grid(row=2, column=1, padx=6, pady=6)

window.mainloop()
