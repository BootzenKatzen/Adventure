import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import font
import re

class AdventureGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Choose Your Own Adventure Game")

        # Define the desired font
        self.custom_font = font.Font(family="Arial", size=14)

        # Set up the scrolled text widget
        self.story_text = scrolledtext.ScrolledText(root, font=self.custom_font, state=tk.DISABLED, wrap=tk.WORD)
        self.story_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Set up the entry widget
        self.entry = tk.Entry(root, font=self.custom_font)
        self.entry.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.entry.bind("<Return>", self.handle_choice)
        # Start the game
        self.start_game()

    def load_story_part(self, filename):
        folder_name = "stories"  # Name of the subfolder
        path = f"{folder_name}/{filename}"
        try:
            with open(path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Story part not found."


    def display_story_part(self, story_part):
        # Create a new bold font object and define a highlight tag
        bold_font = font.Font(family="Arial", size=14, weight='bold')
        highlight_color = 'PaleGreen'  # Choose a highlight color

        self.story_text.config(state=tk.NORMAL)
        self.story_text.delete('1.0', tk.END)  # Clear the current text

        # Split the story part by '**' and process for bold and highlight formatting
        parts = re.split(r'(\*\*.*?\*\*)', story_part)
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                # Remove the asterisks and apply the bold and highlight tags
                bold_text = part[2:-2]
                self.story_text.insert(tk.END, bold_text, ('bold', 'highlight'))
            else:
                self.story_text.insert(tk.END, part)
        self.story_text.tag_configure('bold', font=bold_font)
        self.story_text.tag_configure('highlight', background=highlight_color)

        self.story_text.config(state=tk.DISABLED)
        self.story_text.yview(tk.END)
        # Check if the story part contains "THE END"
        if "THE END" in story_part:
            self.play_again()

    def handle_choice(self, event=None):
        choice = self.entry.get().replace(' ', '_')
        self.entry.delete(0, tk.END)
        next_part = f"{choice.lower()}.txt"
        story_part = self.load_story_part(next_part)
        self.display_story_part(story_part)

    def start_game(self, from_play_again=False):

        if not from_play_again:
            # Ask the player if they have played before only if not coming from play again
            played_before = simpledialog.askstring("Welcome!", "Hello! Welcome! Have you played before? (yes/no)")
            if played_before and played_before.lower() == 'no':
                # If the player is new, show the introduction
                intro_part = "introduction.txt"
                story_part = self.load_story_part(intro_part)
                self.display_story_part(story_part)
                return  # Return early to avoid asking for a keyword

        # If the player has played before or is coming from play again, ask for a keyword
        self.root.update_idletasks()  # Update the main window
        self.root.attributes('-topmost', False)  # Temporarily set the main window on top
        keyword_dialog = simpledialog.askstring("Keyword", "Enter a previous choice (i.e. left or right) to start from a specific part of the story (leave blank to start from the beginning):")
        self.root.attributes('-topmost', True)  # Set the main window back to normal

        if keyword_dialog:  # If the dialog is not None, bring it to the front
            self.root.tkraise()

        start_part = "beginning.txt" if not keyword_dialog else f"{keyword_dialog.lower()}.txt"
        story_part = self.load_story_part(start_part)
        self.display_story_part(story_part)

    def play_again(self):
        answer = simpledialog.askstring("Play Again", "Do you want to play again? (yes/no)")
        if answer and answer.lower() == 'yes':
            self.story_text.config(state=tk.NORMAL)
            self.story_text.delete('1.0', tk.END)
            self.story_text.config(state=tk.DISABLED)
            self.start_game(from_play_again=True)
        else:
            self.root.quit()

# Main window setup
root = tk.Tk()
app = AdventureGame(root)
root.mainloop()
