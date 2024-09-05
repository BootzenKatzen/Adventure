import tkinter as tk
from tkinter import simpledialog, scrolledtext, font, messagebox
import re
import os

class CustomAskString(simpledialog.Dialog):

    """
    Custom "simpledialog" to fix error
    Was previously not focusing on the dialogue on the second loop
    needed the after and focus force to get it to cooperate
    """

    def __init__(self, parent, title, prompt):

        self.prompt = prompt  # Store the prompt as an instance variable
        super().__init__(parent, title=title)  # Only pass the accepted arguments to the superclass

    def body(self, master):

        self.label = tk.Label(master, text=self.prompt) # Use the stored prompt for the label
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.after(1, lambda: self.entry.focus_force())

    def apply(self):
        self.result = self.entry.get()  # Get the input from the entry widget

def ask_custom_string(title, prompt, parent):

    dialog = CustomAskString(parent, title, prompt)
    return dialog.result

class AdventureGame:

    def __init__(self, root):
        self.root = root

        self.root.title("Choose Your Own Adventure Game")
        self.valid_choices = []
        self.current_story_part = ''

        # Define the desired font
        self.custom_font = font.Font(family="Calibri", size=16)

        # Set up the scrolled text widget
        self.story_text = scrolledtext.ScrolledText(root, font=self.custom_font, state=tk.DISABLED, wrap=tk.WORD)
        self.story_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.story_text.tag_configure(
        'bold', font=(self.custom_font.actual('family'),
        self.custom_font.actual('size'), 'bold')
        )

        self.story_text.tag_configure(
        'highlight', font=(self.custom_font.actual('family'),
        self.custom_font.actual('size'), 'bold'), background="PaleGreen"
        )
        # Set up the entry widget
        self.entry = tk.Entry(root, font=self.custom_font)
        self.entry.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.entry.bind("<Return>", self.handle_choice)
        # Start the game
        self.start_game()

    def get_story_filenames(self):
        folder_name = "stories"  # Name of the subfolder where your story parts are stored
        # List all files in the directory
        files = os.listdir(folder_name)
        # Filter out only .txt files and remove the file extension
        txt_files = [os.path.splitext(file)[0] for file in files if file.endswith('.txt')]
        return txt_files

    def find_valid_choices(self, story_part):
        # Use a regular expression to find all instances of text surrounded by double asterisks
        choices = re.findall(r'\*\*(.*?)\*\*', story_part)
        # Remove duplicates and convert to lowercase
        valid_choices = list(set(choice.replace(' ', '_').lower() for choice in choices))
        return valid_choices

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
        self.current_story_part = story_part
        self.valid_choices = self.find_valid_choices(story_part)
        # Enable the text widget for editing
        self.story_text.config(state=tk.NORMAL)

        # Insert the new story part at the end
        parts = re.split(r'(\*\*.*?\*\*|@@.*?@@)', story_part)
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                # Remove the asterisks and apply the bold and highlight tags
                highlight_text = part[2:-2]
                self.story_text.insert(tk.END, highlight_text, ('highlight'))
            elif part.startswith('@@') and part.endswith('@@'):
                bold_text = part[2:-2]
                self.story_text.insert(tk.END, bold_text, ('bold'))
            else:
                self.story_text.insert(tk.END, part)

        # add deliniation between story parts
        self.story_text.insert(tk.END, "\n\n" + "_" * 50 + '\n\n')

        # Disable editing again
        self.story_text.config(state=tk.DISABLED)

        # Scroll to the end
        self.story_text.yview(tk.END)

        # Check if the story part contains "THE END"
        if "THE END" in story_part:
            self.play_again()

    def handle_choice(self, event=None):
        choice = self.entry.get().replace(' ', '_').capitalize()
        if choice.lower() in self.valid_choices:
            next_part = f"{choice.lower()}.txt"
            story_part = self.load_story_part(next_part)
            self.display_story_part(story_part)
        elif choice.lower() == 'quit':
            self.root.quit()
        else:
            # If the input is not a valid choice, display an error message and repeat the last part
            self.display_story_part("I'm sorry, I didn't understand that. Please try again.\n\n" + self.current_story_part)
        self.entry.delete(0, tk.END)

    def start_game(self, from_play_again=False):

        self.valid_choices = self.get_story_filenames()
        if not from_play_again:
            # Ask the player if they have played before only if not coming from play again
            while True:
                played_before = simpledialog.askstring("Welcome!", "Hello! Welcome! Have you played before? (yes/no)", parent=root)
                if played_before and played_before.lower() in ['yes', 'no']:
                    break
                else:
                    messagebox.showerror("Invalid Input", "Please type 'yes' or 'no'")
            if played_before and played_before.lower() == 'no':
                # If the player is new, show the introduction
                self.entry.focus_force()
                intro_part = "introduction.txt"
                story_part = self.load_story_part(intro_part)
                self.display_story_part(story_part)
                return  # Return early to avoid asking for a keyword

        self.root.update_idletasks()  # Update the main window
        while True:
            keyword_dialog = ask_custom_string("Keyword", "Enter a previous choice (i.e. left or right) to start from a specific part of the story (leave blank to start from the beginning):", parent=self.root).replace(" ", "_")
            if keyword_dialog is None or keyword_dialog == '' or keyword_dialog.capitalize() in self.valid_choices:
                break
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid choice or leave blank to start from the beginning.")

        start_part = "begin.txt" if not keyword_dialog else f"{keyword_dialog.capitalize()}.txt"
        story_part = self.load_story_part(start_part)
        self.display_story_part(story_part)
        self.entry.focus_force()

    def play_again(self):
        while True:
            answer = ask_custom_string("Play Again", "Do you want to play again? (yes/no)", parent=root)
            if answer and answer.lower() in ['yes', 'no']:
                break
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid choice or leave blank to start from the beginning.")
        if answer and answer.lower() == 'yes':
            self.story_text.config(state=tk.NORMAL)
            self.story_text.delete('1.0', tk.END)
            self.story_text.config(state=tk.DISABLED)
            self.root.update_idletasks()
            self.start_game(from_play_again=True)
            self.root.update_idletasks()
        else:
            self.root.quit()

# Main window setup
root = tk.Tk()
app = AdventureGame(root)
root.mainloop()
