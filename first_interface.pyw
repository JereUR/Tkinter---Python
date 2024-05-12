from tkinter import Tk, Label, Button


def message():
    print('Button message')


window = Tk()

window.title('Test window')

window.iconbitmap('logo.ico')

window.geometry('650x450')

lbl = Label(window, text='This is a Tkinter Label')
lbl.pack()

btn = Button(
    window, text='Push this Button to show message', command=message)
btn.config(bg='yellow')
btn['fg'] = 'red'
btn.pack()

window.mainloop()
