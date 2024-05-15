from tkinter import Button, Frame, Tk

window = Tk()
window.title('Fram example')
window.geometry('200x70')

frame1 = Frame(window, bg='blue')
frame1.pack(expand=True, fill='both')

frame2 = Frame(window, bg='yellow')
frame2.pack(expand=True, fill='both')
frame2.config(cursor='heart')

redButton = Button(frame1, text='Red', fg='red')
greenButton = Button(frame1, text='Green', fg='green')
blueButton = Button(frame1, text='Blue', fg='blue')

redButton.place(relx=.05, rely=.05, relwidth=.25, relheight=.9)
greenButton.place(relx=.35, rely=.05, relwidth=.25, relheight=.9)
blueButton.place(relx=.65, rely=.05, relwidth=.25, relheight=.9)

blackButton = Button(frame2, text='Black', fg='black')
blackButton.pack()


window.mainloop()
