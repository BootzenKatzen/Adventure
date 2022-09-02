import tkinter as tk

import tkinter.scrolledtext as st

from time import sleep

def PZ():
    sleep(1)

# need to look into the .after method to add the pauses between lines.

def print1(text):
    txt.configure(state = 'normal')
    txt.insert(tk.END,"\n")
    txt.insert(tk.END, text)
    txt.configure(state = 'disabled')
    txt.see(tk.END)
    #PZ()

def print2(text):
    txt.configure(state = 'normal')
    txt.insert(tk.END,"\n")
    txt.insert(tk.END, text)
    txt.insert(tk.END,"\n")
    txt.configure(state = 'disabled')
    txt.see(tk.END)
    #PZ()

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()
bottomframe = tk.Frame(root)
bottomframe.pack( side = tk.BOTTOM )
root.title("Testing Zone")
root.geometry('350x300')
txt = st.ScrolledText(frame, width='40', height='15', wrap=tk.WORD)
toplabel = tk.Label(frame, text = "Welcome!")
userin = tk.Entry(bottomframe, width = '50')
userin.pack(side = tk.LEFT)

txt.pack(side = tk.BOTTOM)
txt.yview(tk.END)
toplabel.pack(side = tk.TOP)

txt.insert(tk.INSERT, 'Welcome to the Adventure Zone!\n')
txt.insert(tk.INSERT, 'Would you like to play a game?')
txt.configure(state = 'disabled')

def changelabel(text):
    toplabel["text"] = text

def clear_text():
    userin.delete(0, tk.END)

def woods(event=None):
    print1("placeholder")
    pass

def tavern(event=None):
    print1("placeholder")
    pass

def choice1(event=None):
    whereto = userin.get().lower().strip()
    if whereto == "woods":
        print1("The woods are spooky")
        button["command"] = woods
    elif whereto == "tavern":
        print1("The tavern is crowded")
        button["command"] = tavern
    else:
        print1("What?")
        print1("Woods or Tavern?")


def clicked(event=None):
    start = userin.get().lower().strip()
    print1(userin.get())
    clear_text()
    changelabel("Let's go!")
    if start == "y":
        print1("Lets go!")
        print1("Woods or Tavern?")
        button["command"] = choice1
    elif start == "n":
        print1("Ok bye!")
    else:
        print1("What?")
        print1("Do you want to play a game?")

#root.bind('<Return>', clicked)
button = tk.Button(bottomframe, text = "enter", command = clicked)
button.pack(side = tk.RIGHT)
#button2 = tk.Button(bottomframe, text = "enter", command = choice1)
#button3 = tk.Button(bottomframe, text = "enter", command = woods)
#button4 = tk.Button(bottomframe, text = "enter", command = tavern)


"""
def game():
    print1("Do you want to play a game?")
    start = userin.get().lower().strip()
    if start == "y":
        print1("Let's go!")
        changelabel("Adventure Time!")
    elif start == "n":
        print1("Okay bye!")
        changelabel("See ya!")
    else:
        print1("What?")
        game()

game()
"""
root.mainloop()







#txt.insert(INSERT, "More text")
