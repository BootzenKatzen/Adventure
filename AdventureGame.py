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
