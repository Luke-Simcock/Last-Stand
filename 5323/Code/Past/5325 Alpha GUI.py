#Importations
import os
import pygame 
import random
import sys
import time
import threading
from ctypes import windll
from tkinter import *
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_a,
    K_s,
    K_d,
    K_SPACE,
    K_m,
    K_b,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def gui():
    root = Tk()
    root.title('Codemy.com')
    root.iconbitmap('C:/Pictures/Camera Roll/MC.ico')

    app_width = 509
    app_height = 833

    root.geometry(f"{app_width}x{app_height}+{-7}+{0}")

    size = 15
    row_number = 0

    Grid.columnconfigure(root, index=0, weight=1)

    button1 = Button(root, text="Start")
    button2 = Button(root, text="Settings")
    button3 = Button(root, text="Tutorial")
    button4 = Button(root, text="Leaderboard")
    button5 = Button(root, text="Accounts")
    button6 = Button(root, text="Credits")
    button7 = Button(root, text="Quit")

    button1.grid(row=0, column=0, sticky="nsew")
    button2.grid(row=1, column=0, sticky="nsew")
    button3.grid(row=2, column=0, sticky="nsew")
    button4.grid(row=3, column=0, sticky="nsew")
    button5.grid(row=4, column=0, sticky="nsew")
    button6.grid(row=5, column=0, sticky="nsew")
    button7.grid(row=6, column=0, sticky="nsew")

    button1.config(font=("Helvetica", (size)))
    button2.config(font=("Helvetica", (size)))
    button3.config(font=("Helvetica", (size)))
    button4.config(font=("Helvetica", (size)))
    button5.config(font=("Helvetica", (size)))
    button6.config(font=("Helvetica", (size)))
    button7.config(font=("Helvetica", (size)))

    button_list = [button1, 
                   button2, 
                   button3, 
                   button4,
                   button5,
                   button6,
                   button7
                   ]

    for button in button_list:
        Grid.rowconfigure(root, row_number, weight=1)
        row_number += 1

    root.mainloop()
Thread4 = threading.Thread(target=gui)
Thread4.start()