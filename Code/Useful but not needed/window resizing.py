from tkinter import *

root = Tk()
root.title('Codemy.com')
root.iconbitmap('C:/Pictures/Camera Roll/MC.ico')
root.geometry("800x800")

def resize():
    w = width_entry.get()
    h = height_entry.get()
    
    root.geometry(f"{w}x{h}")


width_label = Label(root, text="Width:")
width_label.pack(pady=20,padx=2)
width_entry = Entry(root)
width_entry.pack()

height_label = Label(root, text="Height:")
height_label.pack(pady=20,padx=20)
height_entry = Entry(root)
height_entry.pack()

button1 = Button(root, text="Resize", command=resize)
button1.pack(pady=2)

root.mainloop()