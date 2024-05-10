import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext

class Game:

    def __init__(self, root):

        self.root = root
        self.root.title("Game Window")
        self.entry_widget = tk.Entry(root)
        self.entry_widget.pack()
        self.scrollbox = scrolledtext.ScrolledText(root, width=40, height=10)
        self.scrollbox.pack()

        self.on_open()

    def on_open(self):

        response = simpledialog.askstring("Question", "Have you played before?")
        if response is not None:
            if response.lower() == "no":
                self.scrollbox.insert(tk.END, "Welcome!\n")
            elif response.lower() == "yes":
                self.scrollbox.insert(tk.END, "Let's play!\n")

root = tk.Tk()
app = Game(root)
root.mainloop()
