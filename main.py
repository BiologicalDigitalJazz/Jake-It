from tkinter import *

blue = "#7289DA"
grey = "#2C2F33"
darkgrey = "#23272A"
white = "#FFFFFF"
green = "#2E8B57"
red = "#DC143C"

root = Tk()
root.title("Jake It")
root.configure(bg=darkgrey)
root.resizable(False, False)

version = Label(root, text="v1.2", fg=blue, bg=darkgrey)
version.place(x=0, y=0)

textlabel = Label(root, text="Jessage Jo Jake", fg=blue, bg=darkgrey)
textlabel.grid(row=6, column=0)
jaketext = Text(root, width=200, borderwidth=5, fg=white, bg=grey)
jaketext.grid(row=7, column=0)

allowed = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def convert(string):
    li = list(string.split(" "))
    return li


def jake():
    message = jaketext.get("1.0", END)
    message = message.replace("  ", " ")
    message = convert(message)
    jessage = ""
    piss = 0
    while piss in range(len(message)):
        holding = message[piss]
        if holding[0] in allowed and holding[0].isupper() is True:
            jessage += "J" + holding.replace(holding[0], holding[0].lower(), 1) + " "
        elif holding[0] in allowed:
            jessage += "j" + holding + " "
        elif holding[0].isupper() is True:
            jessage += holding.replace(holding[0], "J", 1) + " "
        else:
            jessage += holding.replace(holding[0], "j", 1) + " "
        piss += 1

    jaketext.delete(1.0, "end")
    jaketext.insert(1.0, jessage)


jakebutton = Button(root, text="Jake It", padx=10, pady=10, command=jake, fg=white, bg=green)
jakebutton.grid(row=8, column=0)

root.mainloop()
