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

txt.insert(tk.INSERT, 'Welcome to the Adventure Zone!')
txt.configure(state = 'disabled')


def changelabel(text):
    toplabel["text"] = text

def clear_text():
    userin.delete(0, tk.END)

def clicked(event=None):
    print1(userin.get())
    clear_text()
    changelabel("Let's go!")

root.bind('<Return>', clicked)

button = tk.Button(bottomframe, text = "enter", command = clicked)
button.pack(side = tk.RIGHT)

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
