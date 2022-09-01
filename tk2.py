
import tkinter as tk

import tkinter.scrolledtext as st


class SampleApp(tk.Tk):

    def print1(self, text):
        self.txt.configure(state = 'normal')
        self.txt.insert(tk.END,"\n")
        self.txt.insert(tk.END, text)
        self.txt.configure(state = 'disabled')
        self.txt.see(tk.END)
        #PZ()

    def print2(self, text):
        self.txt.configure(state = 'normal')
        self.txt.insert(tk.END,"\n")
        self.txt.insert(tk.END, text)
        self.txt.insert(tk.END,"\n")
        self.txt.configure(state = 'disabled')
        self.txt.see(tk.END)
        #PZ()

    def changelabel(self, text):
        self.toplabel["text"] = text

    def clear_text(self):
        self.userin.delete(0, tk.END)

    def clicked(self, event=None):
        self.print1(self.userin.get())
        self.clear_text()
        self.changelabel("Let's go!")

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Testing Zone")
        self.geometry('350x300')
        self.frame = tk.Frame(self)
        self.bottomframe = tk.Frame(self)
        self.txt = st.ScrolledText(self.frame, width='40', height='15', wrap=tk.WORD)
        self.txt.yview(tk.END)
        self.toplabel = tk.Label(self.frame, text = "Welcome!")
        self.userin = tk.Entry(self.bottomframe, width = '50')
        self.button = tk.Button(self.bottomframe, text = "enter", command = self.clicked)
        self.frame.pack()
        self.bottomframe.pack(side = tk.BOTTOM)
        self.toplabel.pack(side = tk.TOP)
        self.txt.pack(side = tk.BOTTOM)
        self.userin.pack(side = tk.LEFT)
        self.button.pack(side = tk.RIGHT)

        self.bind('<Return>', self.clicked)

        self.txt.configure(state = 'normal')
        self.txt.insert(tk.END, "Welcome!")
        self.txt.configure(state = 'disabled')
        self.txt.see(tk.END)



def game():
    print1("Would you like to go on an adventure? [Y/N]")
    start = self.userin.get().lower().strip()
    if start == "y":
        self.print1("Let's go!")
    elif start == "n":
        self.print1("Okay, bye!")
    else:
        self.print1("What?")
        game()

game()


w = SampleApp()
w.mainloop()
