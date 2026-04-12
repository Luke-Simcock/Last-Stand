from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Codemy.com')
root.iconbitmap('C:/Pictures/Camera Roll/MC.ico')

app_width = 1535
app_height = 833

root.geometry(f"{app_width}x{app_height}+{-7}+{0}")

size = 40
row_number = 0



def open_txt_signin():
    file = open("C:/TextFolders Data/AccountUsernames.txt", 'r')
    read = file.readlines()
    modified = []

    for line in read:
        if line not in modified:
            modified.append(line.strip())

    print(modified)
    file.close()

def open_txt_signup():
    file = open("C:/TextFolders Data/AccountPasswords.txt", 'a')

    username = ['Adrian']
    password = ['verysecure@indeed']

    entry = username[0]+ "-" + str(password[0])+'\n'
    file.write(entry)

    file.close()

def validate_length():

    username = signupin_username_entry.get()
    password = signupin_password_entry.get()

    if len(username) == 5:
        print("True")
    else:
        print("Please Enter a ")
    
    if len(password) == 6:
        print("True")
    else:
        print("False")



# vertical / y
Grid.rowconfigure(root, index=0, weight=1)
Grid.rowconfigure(root, index=1, weight=1)
Grid.rowconfigure(root, index=2, weight=1)
Grid.rowconfigure(root, index=3, weight=1)
Grid.rowconfigure(root, index=4, weight=1)
Grid.rowconfigure(root, index=5, weight=1)
Grid.rowconfigure(root, index=6, weight=1)

# horisontal / x
Grid.columnconfigure(root, index=0, weight=1)
Grid.columnconfigure(root, index=1, weight=3)
Grid.columnconfigure(root, index=2, weight=3)
Grid.columnconfigure(root, index=3, weight=1)

signupin_username_label = Label(root, text="Username:")
signupin_username_entry = Entry(root)
signupin_password_label = Label(root, text="Password:")
signupin_password_entry = Entry(root)
signin = Button(root, text="Sign Up:", command=validate_length)
signup = Button(root, text="Sign In:", command=validate_length)

signupin_username_label.grid(row=1, column=1, sticky="nsew")
signupin_username_entry.grid(row=1, column=2, sticky="nsew")
signupin_password_label.grid(row=3, column=1, sticky="nsew")
signupin_password_entry.grid(row=3, column=2, sticky="nsew")
signin.grid                 (row=5, column=1, sticky="nsew")
signup.grid                 (row=5, column=2, sticky="nsew")

signupin_username_label.config(font=("Helvetica", (size)))
signupin_username_entry.config(font=("Helvetica", (size)))
signupin_password_label.config(font=("Helvetica", (size)))
signupin_password_entry.config(font=("Helvetica", (size)))
signin.config                 (font=("Helvetica", (size)))
signup.config                 (font=("Helvetica", (size)))


button_list = [signupin_username_label,
               signupin_username_entry,
               signupin_password_label,
               signupin_password_entry,
               signup,
               signup
               ]

# Test with different values


root.mainloop()