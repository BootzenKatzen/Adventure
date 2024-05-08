"""
Alrighty! Let's get this started!  I'm going to try and merge the GUI from
the tk.py file with the content from the Adventures2.py file.

I'll kind of have to think of the content backwards, since that's how it
works once the buttons are involved.

Instead of fluff text -> choice given -> choice -> new function -> new text

It has to be text -> choice given -> button press for choice ->
new text -> new choice -> new function assigned to button
"""
import tkinter as tk  # needed for gui

import tkinter.scrolledtext as st  # for text box

import os # for grabbing text files

texts = {} # a dictionary for filenames and their texts
           # this will be used to pull formatted text into the game

path = 'txt_files/'

for f in os.scandir(path):
    if (f.path.endswith(".txt")
                ) and f.is_file():
                file_name, ext = os.path.splitext(os.path.basename(f))
                o = open(f)
                contents = o.read()
                texts[file_name] = contents

# the above loops through the contents of the folder
# if the file ends with .txt and is a file
# we split the filename into name and extension (.txt)
# the name is stored as variable file_name
# we read the contents of the file into a variable
# then add a filename: contents entry to the dictionary

# establish game fonts
font1 = ("Arial", 16, "bold")  # normal font for label
font2 = ("Arial", 12, "normal")  # for button and text
font3 = ("Algerian", 20)  # starting font for label for big "Welcome"

# creating methods to add text to the text box, but keep it from being
# editable by the player


def add_text1(text):  # opens scrollbox for editing, prints on new line, closes

    """
    Makes the scrollbox widget editable to add new text
    Adds the text
    Then makes it uneditable again
    """

    txt.configure(state='normal')
    txt.insert(tk.END, "\n")
    txt.insert(tk.END, text)
    txt.configure(state='disabled')
    txt.see(tk.END)


def add_text2(text):  # same as print 1 but leaves a blank line after

    """
    Makes the scrollbox uneditable
    Adds the new text (and a blank line)
    Makes it uneditable again
    """

    txt.configure(state='normal')
    txt.insert(tk.END, "\n")
    txt.insert(tk.END, text)
    txt.insert(tk.END, "\n\n")
    txt.insert(tk.END, "     *   *   *   *   *   *   *     \n")
    txt.configure(state='disabled')
    txt.see(tk.END)

def story(text):

    add_text1(texts[text])

def change_cmd(function):

    """
    Method for changing the command of the button and return key at the
    same time, to swap the commands for the choice tree
    """

    button["command"] = function
    root.bind('<Return>', function)


def uip():

    """
    uip stands for "User InPut"
    Pulls data from the entry widget
    """

    return userin.get()


def uip_low():

    """
    Pulls the user input but makes it lowercase and strips punctuation
    for downstream uses
    """

    return userin.get().lower().strip()


def ui_text():

    """
    gets the user input, and prints it in the scrollbox
    """
    add_text2(uip())

def ui_choice():

    temp = uip_low()
    ui_text()
    empty()
    return temp

def nutext(text):

    """
    way to easily change the global vairable in a function
    allows for changing the text in the choice three
    so it can easily be repeated as necessary

    cu_te - stands for "CUrrent TExt"
    """

    globals()["cu_te"] = text


def quest(text):

    """
    Asks the question and changes the variable in one step
    """

    nutext(texts[text])
    add_text1(texts[text])


def what():

    """
    function for repeating the choice if the input doesn't match
    any of the if/else statements
    """

    add_text1("What was that? I didn't understand.\n")
    add_text1(cu_te)


root = tk.Tk()  # creating main window

bottomframe = tk.Frame(root)
# creating bottom frame to put entry and button in
bottomframe.grid(column=0, row=2, sticky='ew')
root.title("Adventure Zone")  # setting window bar label
root.geometry('500x500')  # setting window size
txt = st.ScrolledText(root, width='40', height='15', wrap=tk.WORD)
# not sure if setting scrolled text size is important since it's sticky
txt.configure(font=font2, spacing2=12)
toplabel = tk.Label(root, text="Welcome!")  # label above text widget
toplabel.configure(font=font3)
userin = tk.Entry(bottomframe, width='60')  # entry widget user interacts with
userin.grid(column=0, row=0, sticky="ew")
userin.focus_set()
# place entry widget to the left in the bottom frome - expands to fit window

txt.grid(column=0, row=1, sticky="nsew")
# makes text entry expand sideways to window size
txt.yview(tk.END)  # always scrolls to newest text
toplabel.grid(column=0, row=0, ipady=10, sticky='ew')
# placing the label at the top of the window - centered

txt.insert(tk.INSERT, 'Welcome to the Adventure Zone!\n\n')
# inserting starting text into widget
cu_te = "Would you like to play a game? (Y/N)\n"
# setting starting "Current Text" to begin game
txt.insert(tk.INSERT, cu_te) # first choice prompt
txt.configure(state='disabled')  # makes scrollbox uneditable


def change_label(text):

    """
    function to change the text of the label
    want to later impliment "bookmarks"
    """
    toplabel["text"] = text


def empty():

    """
    empties the entry box - for use after button press
    """

    userin.delete(0, tk.END)


def placeholder():

    """
    placeholder event to allow for playtesting
    """

    add_text1("Placeholder")
    again()
    pass


def drink(event=None):

    placeholder()

def eat(event=None):

    placeholder()

def look_around(event=None):

    placeholder()

def which_trail(event=None):

    whereto = uip_low()
    if whereto == "a":
        story('meadow')
        quest('meadow_choices')
        change_cmd(meadow)
    elif whereto == 'b':
        change_cmd(woods)
    else:
        what()

    placeholder()

def woods(event=None):
    ui_text()
    empty()
    placeholder()

def meadow(event=None):

    whereto = uip_low()
    if whereto == 'a':
        placeholder()
    elif whereto == 'b':
        placeholder()
    elif whereto == 'c':
        change_cmd()


def tavern(event=None):  # placeholder event

    whereto = uip_low()
    empty()
    if whereto == "a":
        quest("approach_bar")
        change_cmd(drink)
    elif whereto == 'b':
        quest("ask_menu")
        change_cmd(eat)
    elif whereto == 'c':
        quest("look_around")
        change_cmd(look_around)
    else:
        what()



def choice1(event=None):

    """
    First choice in the adventure
    Can be used as a template for further choices
    I'll only add notes to this one since the others should be functionally
    the same.
    """

    ui_text()  # will print the user input after button click
    whereto = uip_low()  # uses lowercase version of input for variable
    empty()  # empties entry widget
    if whereto == "n":
        # This will have descriptions of the next event
        # as well as the next choice to be made
        story('outdoors')
        quest('woods_or_meadow')
        change_cmd(which_trail)
        # changes button command to the next event
        # so it's prepared to recieve the next input
    elif whereto == "y":
        story('enter_tavern')
        quest('tavern_choice')
        # same as "woods" but going to a different event
        change_cmd(tavern)
    else:
        what()
        # in case the user has a typo or something we want to alert them.
        # and then reiterate the choice

# first button click function - basic start of game
# need to add exit if they choose not to play

#def name_get(text):

    #globals()["u_name"] = text


def greeting1():

    nutext("What is your name, adventurer?")
    add_text1("What is your name, adventurer?")
    change_cmd(greeting2)


def greeting2(event=None):

    globals()['u_name'] = ui_choice()
    greetings = "Hello " + u_name + "! Let's go!\n"
    add_text2(greetings)
    first_begin()

def begin():

    """
    Keeping the beginning option separate so we can loop back to it if the
    player wants to play again.
    """

    story('starting_text')
    quest('q_enter_tavern')
    change_cmd(choice1)

def first_begin(event=None):

    root.after(1000, begin)


def again():

    quest("play_again")
    play_again = ui_choice()
    if play_again == 'y':
        begin()
    elif play_again == 'n':
        end_game()
    else:
        what()

def end_game():

    """
    Creating routine for when player decides to leave the game
    """
    add_text1("Ok bye!")
    add_text1("Quitting game...")
    root.after(2000, root.destroy)

def clicked(event=None):

    """
    Starting text and first choice in the game
    The first button click functionally
    Quits game if user decides not to play
    """
    whereto = ui_choice()
    #ui_text()
    #start = uip_low()
    #empty()
    toplabel.configure(font=font1)
    change_label("Let's go!")
    if whereto == "y":
        greeting1()
    elif whereto == "n":
        end_game()
    else:
        what()



button = tk.Button(bottomframe, text="Enter", font=font2, command=clicked)
# creating button
button.grid(column=1, row=0, ipadx=10, sticky="e")
# button sticks to right hand side and doesn't change with the window

root.bind('<Return>', clicked)  # return key = button click

bottomframe.grid_columnconfigure(0, weight=1)
# adding weight so the widgets expand
bottomframe.grid_columnconfigure(1, weight=0)

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=2)
root.grid_rowconfigure(2, weight=0)
root.grid_columnconfigure(0, weight=1)

root.mainloop()  # starts GUI/game
