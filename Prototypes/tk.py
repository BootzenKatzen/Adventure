import tkinter as tk

import tkinter.scrolledtext as st

from time import sleep

def PZ():
    sleep(1)

font1 = ("Arial", 16, "bold")
font2 = ("Arial", 12, "normal")
font3 = ("Algerian", 20)
# need to look into the .after method to add the pauses between lines.

def print1(text): # open's scrollbox for editing, prints on new line, closes
    txt.configure(state = 'normal')
    txt.insert(tk.END,"\n")
    txt.insert(tk.END, text)
    txt.configure(state = 'disabled')
    txt.see(tk.END)
    #PZ()

def print2(text): # same as print 1 but leaves a blank line after
    txt.configure(state = 'normal')
    txt.insert(tk.END,"\n")
    txt.insert(tk.END, text)
    txt.insert(tk.END,"\n")
    txt.configure(state = 'disabled')
    txt.see(tk.END)
    #PZ()

def changecmd(function):
    button["command"] = function
    root.bind('<Return>', function)

def uip(): # stands for User InPut - shorthand for pulling input from Entry Widget
    return userin.get()

def uiplow(): #User InPut but lower case - strips input for downstream uses
    return userin.get().lower().strip()

def uiprint(): #gets user input, prints it, and then strips it
    print1(uip())


root = tk.Tk()

#frame = tk.Frame(root)
#frame.pack()
bottomframe = tk.Frame(root)
bottomframe.grid(column=0, row =2, sticky = 'ew')
root.title("Testing Zone")
root.geometry('500x500')
txt = st.ScrolledText(root, width='40', height='15', wrap=tk.WORD)
txt.configure(font = font2)
toplabel = tk.Label(root, text = "Welcome!")
toplabel.configure(font = font3)
userin = tk.Entry(bottomframe, width = '60')
userin.grid(column=0, row=0, sticky="ew")

txt.grid(column=0, row=1, sticky="nsew")
txt.yview(tk.END)
toplabel.grid(column = 0, row = 0, ipady = 10, sticky='ew')

txt.insert(tk.INSERT, 'Welcome to the Adventure Zone!\n')
txt.insert(tk.INSERT, 'Would you like to play a game?')
txt.configure(state = 'disabled')

def changelabel(text):
    toplabel["text"] = text

def empty():
    userin.delete(0, tk.END)

def woods(event=None):
    print1("placeholder")
    pass

def tavern(event=None):
    print1("placeholder")
    pass

def choice1(event=None):
    uiprint()
    whereto = uiplow()
    empty()
    if whereto == "woods":
        print1("The woods are spooky")
        changecmd(woods)
    elif whereto == "tavern":
        print1("The tavern is crowded")
        changecmd(tavern)
    else:
        print1("What?")
        print1("Woods or Tavern?")


def clicked(event=None):
    uiprint()
    start = uiplow()
    empty()
    toplabel.configure(font = font1)
    changelabel("Let's go!")
    if start == "y":
        print1("Lets go!")
        print1("Woods or Tavern?")
        changecmd(choice1)
    elif start == "n":
        print1("Ok bye!")
    else:
        print1("What?")
        print1("Do you want to play a game?")


button = tk.Button(bottomframe, text = "Enter", font = font2, command = clicked)
button.grid(column = 1, row = 0, ipadx = 10, sticky = "e")

root.bind('<Return>', clicked)

bottomframe.grid_columnconfigure(0, weight =1)
bottomframe.grid_columnconfigure(1, weight = 0)

root.grid_rowconfigure(0, weight = 0)
root.grid_rowconfigure(1, weight = 2)
root.grid_rowconfigure(2, weight = 0)
root.grid_columnconfigure(0, weight = 1)

root.mainloop()
