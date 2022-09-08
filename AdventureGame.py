# Alrighty! Let's get this started!  I'm going to try and merge the GUI from
# the tk.py file with the content from the Adventures2.py file.

#I'll kind of have to think of the content backwards, since that's how it works
#once the buttons are involved.

#Instead of fluff text -> choice given -> choice -> new function -> new text

#It has to be text -> choice given -> button press for choice ->
#new text -> new choice -> new function assigned to button

import tkinter as tk #needed for gui

import tkinter.scrolledtext as st #for text box

#establish game fonts
font1 = ("Arial", 16, "bold")  #normal font for label
font2 = ("Arial", 12, "normal")#for button and text
font3 = ("Algerian", 20) #starting font for label for big "Welcome"


#creating methods to add text to the text box, but keep it from being
#editable by the player
def print1(text): # open's scrollbox for editing, prints on new line, closes
    txt.configure(state = 'normal')
    txt.insert(tk.END,"\n")
    txt.insert(tk.END, text)
    txt.configure(state = 'disabled')
    txt.see(tk.END)

def print2(text): # same as print 1 but leaves a blank line after
    txt.configure(state = 'normal')
    txt.insert(tk.END,"\n")
    txt.insert(tk.END, text)
    txt.insert(tk.END,"\n")
    txt.configure(state = 'disabled')
    txt.see(tk.END)

#method for changing the command of the button and the return key at the same
#time to make it easier to swap commands for the choice tree
def changecmd(function):
    button["command"] = function
    root.bind('<Return>', function)

def uip(): # stands for User InPut - shorthand for pulling input from Entry Widget
    return userin.get()

def uiplow(): #User InPut but lower case - strips input for downstream uses
    return userin.get().lower().strip()

def uiprint(): #gets user input, prints it, and then strips it
    print1(uip())

root = tk.Tk() #creating main window

bottomframe = tk.Frame(root) #creating bottom frame to put entry and button in
bottomframe.grid(column=0, row =2, sticky = 'ew')
root.title("Adventure Zone") #setting window bar label
root.geometry('500x500') #setting window size
txt = st.ScrolledText(root, width='40', height='15', wrap=tk.WORD)
#not sure if setting scrolled text size is important since it's sticky,
txt.configure(font = font2)
toplabel = tk.Label(root, text = "Welcome!") #label above text widget
toplabel.configure(font = font3)
userin = tk.Entry(bottomframe, width = '60') #entry widget user interacts with
userin.grid(column=0, row=0, sticky="ew") #place entry widget to the left in the bottom frome - expands to fit window

txt.grid(column=0, row=1, sticky="nsew") #makes text entry expand sideways to window size
txt.yview(tk.END) #always scrolls to newest text
toplabel.grid(column = 0, row = 0, ipady = 10, sticky='ew') #placing the label at the top of the window - centered

txt.insert(tk.INSERT, 'Welcome to the Adventure Zone!\n') #inserting starting text into widget
txt.insert(tk.INSERT, 'Would you like to play a game?') #first choice prompt
txt.configure(state = 'disabled') #makes scrollbox uneditable

def changelabel(text): #function to change the text of the label - want to later impliment "bookmarks"
    toplabel["text"] = text

def empty(): #empties the entry box - for use after button press
    userin.delete(0, tk.END)


def woods(event=None): #placeholder event
    print1("placeholder")
    pass

def tavern(event=None): #placeholder event
    print1("placeholder")
    pass

def choice1(event=None): #first choice - used for testing GUI function
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
