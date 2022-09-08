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
