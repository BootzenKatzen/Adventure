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

def nutext(text): #way to easily change the global vairable in a function
    globals()["cu_te"] = text

def what(): # function for completing if/else statements - repeats choice
    print1("What?")
    print1(cu_te)

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
cu_te = "Would you like to play a game?"
txt.insert(tk.INSERT, cu_te) #first choice prompt
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

#this is an example of a choice function in the game - I'll only note this one since the others should be the same
def choice1(event=None): #first choice - used for testing GUI function
    uiprint() #will print the user input after button click
    whereto = uiplow() #uses lowercase version of input for variable
    empty() #empties entry widget
    if whereto == "woods":
        nutext("The woods are spooky")
        print1(cu_te)#This will have descriptions of the next event, as well as the next choice to be made
        changecmd(woods) #changes button command to the next event so it's prepared to recieve the next input
    elif whereto == "tavern":
        print1("The tavern is crowded") #same as "woods" but going to a different event
        changecmd(tavern)
    else:
        what() #in case the user has a typo or something we want to alert them.
        #print1("Woods or Tavern?") #prompts the user with the current choice - the button command remains the same for now

#first button click function - basic start of game  - need to add exit if they choose not to play
def clicked(event=None):
    uiprint()
    start = uiplow()
    empty()
    toplabel.configure(font = font1)
    changelabel("Let's go!")
    if start == "y":
        print1("Lets go!")
        nutext("Woods or Tavern?")
        print1(cu_te)
        changecmd(choice1)
    elif start == "n":
        print1("Ok bye!")
    else:
        what()



button = tk.Button(bottomframe, text = "Enter", font = font2, command = clicked) #creating button
button.grid(column = 1, row = 0, ipadx = 10, sticky = "e") #button sticks to right hand side and doesn't change with the window

root.bind('<Return>', clicked) #return key = button click

bottomframe.grid_columnconfigure(0, weight =1) #adding weight so they expand
bottomframe.grid_columnconfigure(1, weight = 0)

root.grid_rowconfigure(0, weight = 0)
root.grid_rowconfigure(1, weight = 2)
root.grid_rowconfigure(2, weight = 0)
root.grid_columnconfigure(0, weight = 1)

root.mainloop() #starts GUI/game
