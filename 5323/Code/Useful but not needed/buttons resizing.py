from tkinter import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('C:/Pictures/Camera Roll/MC.ico')

app_width = 509
app_height = 833

root.geometry(f"{app_width}x{app_height}+{-7}+{0}")

size = 15
row_number = 0

Grid.columnconfigure(root, index=0, weight=1)

button1 = Button(root, text="Button")
button2 = Button(root, text="Button")
button3 = Button(root, text="Button")
button4 = Button(root, text="Button")

button1.grid(row=0, column=0, sticky="nsew")
button2.grid(row=1, column=0, sticky="nsew")
button3.grid(row=2, column=0, sticky="nsew")
button4.grid(row=3, column=0, sticky="nsew")

button1.config(font=("Helvetica", (size)))
button2.config(font=("Helvetica", (size)))
button3.config(font=("Helvetica", (size)))
button4.config(font=("Helvetica", (size)))

button_list = [button1, button2, button3, button4]

for button in button_list:
    Grid.rowconfigure(root, row_number, weight=1)
    row_number += 1

root.mainloop()