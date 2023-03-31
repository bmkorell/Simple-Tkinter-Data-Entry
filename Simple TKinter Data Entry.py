import tkinter as tk
from tkinter import *
import tkinter.messagebox
window = tk.Tk()
window.geometry("645x300")
window.configure(bg="light blue")
window.title("Data Entry")


def submitMessage():
    getName = enterName.get()
    getAge = enterAge.get()
    getGender = variable.get()
    txtBox.insert(tk.INSERT, getName + "\n")
    txtBox.insert(tk.INSERT, getAge + "\n")
    txtBox.insert(tk.INSERT, getGender + "\n" + "\n")
    tkinter.messagebox.showinfo("Success", "Submitted")


name = tk.Label(text="Name", bg="light blue")
name.place(x=0, y=5)

enterName = tk.Entry()
enterName.place(x=50, y=5)

age = tk.Label(text="Age", bg="light blue")
age.place(x=0, y=70)

enterAge = tk.Entry()
enterAge.place(x=50, y=70)

variable = StringVar(window)
variable.set("Select Gender")  # default value

selectGender = OptionMenu(window, variable, "Male", "Female", "Other")
selectGender.config(bg="light blue")
selectGender.place(x=50, y=125)

gender = tk.Label(text="Gender", bg="light blue")
gender.place(x=0, y=125)

submit = tk.Button(text="Submit",
                   command=submitMessage,
                   relief=SUNKEN,
                   height=2,
                   width=21)
submit.place(x=35, y=175)

txtBox = tk.Text(height=20, width=30, bg="light gray")
txtBox.place(x=400, y=0)

window.mainloop()
