import json
from difflib import get_close_matches

data = json.load(open("data.json"))
keys = data.keys()


def translate():
    w = e1_value.get()

    if w in data:
        for i, j in enumerate(data[w]):
            t1.insert(END, str(i) + ' ' + j + '\n')
    elif w.upper() in data:
        for i, j in enumerate(data[w.upper()]):
            t1.insert(END, str(i) + ' ' + j + '\n')
    elif w.title() in data:
        for i, j in enumerate(data[w.title()]):
            t1.insert(END, str(i) + ' ' + j + '\n')
    else:
        list = get_close_matches(w, keys)
        if len(list) == 0:
            t1.insert(END, "The word doesn't exist.Please double check it!")
        else:
            yn = list[0]
            answer = tkinter.messagebox.askquestion("Word Suggestion", "Did you mean " + yn + " instead ?")

            if answer == "yes":
                for i, j in enumerate(data[yn]):
                    t1.insert(END, str(i) + ' ' + j + '\n')
            else:
                t1.insert(END, "The word doesn't exist.Please double check it!")



from tkinter import *
import tkinter.messagebox

root = Tk()

header = Label(root, text="ENGLISH THESAURUS", bg="black", fg="white")
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




root.mainloop()