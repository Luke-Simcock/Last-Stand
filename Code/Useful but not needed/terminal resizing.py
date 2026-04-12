from tkinter import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('C:/Pictures/Camera Roll/MC.ico')
root.geometry("500x500")

button1 = Button(root, text="Button")
button2 = Button(root, text="Button")

button1.grid(row=0, column=0, sticky="nsew")
button2.grid(row=1, column=0, sticky="nsew")


root.mainloop()