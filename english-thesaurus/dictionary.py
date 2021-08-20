import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate():
    w = e1_value.get()
    w = w.lower()
    if w in data:
        return(data)
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = tkinter.messagebox.askquestion("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

def translate2():
    t1.delete(1.0, END)
    e1.delete(0, END)

    translate

from tkinter import *
import tkinter.messagebox

root = Tk()

header = Label(root, text="A Relatively Smart Dictionary", bg="black", fg="white")
header.pack(fill=X)

label1 = Label(root, text="Enter your word:")
label1.pack()

e1_value = StringVar()
e1 = Entry(root, textvariable=e1_value)
e1.pack()

button = Button(root, text="Find meaning!", command=translate, bg="lightgreen")
button.pack()

t1 = Text(root)
t1.pack(fill=X)

label2 = Label(root, text="Hit the button below to search another word!")
label2.pack()

button2 = Button(root, text="Another word!", command=translate2, bg="lightgreen")
button2.pack()


root.mainloop()