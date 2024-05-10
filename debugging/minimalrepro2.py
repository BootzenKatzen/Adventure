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

        self.start_game()

    def start_game(self):

        self.root.update_idletasks()
        response = simpledialog.askstring("Question", "Did you win?", parent=root)
        if response.lower() == "no":
            self.scrollbox.insert(tk.END, "Womp Womp!\n")
            self.play_again()
        elif response.lower() == "yes":
            self.scrollbox.insert(tk.END, "Awesome!\n")
            self.play_again()
        else:
            self.scrollbox.insert(tk.END, "I didn't catch that\n")

    def play_again(self):

        answer = simpledialog.askstring("Play Again", "Do you want to play again? (yes/no)", parent=root)
        if answer and answer.lower() == 'yes':
            self.start_game()

root = tk.Tk()
app = Game(root)
root.mainloop()
