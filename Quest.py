import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext

# Function to load the story part from a file
def load_story_part(filename):
    folder_name = "stories"  # Name of the subfolder
    path = f"{folder_name}/{filename}"
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Story part not found."

# Function to display the story part in the text box
def display_story_part(story_part):
    story_text.config(state=tk.NORMAL)
    story_text.insert(tk.END, story_part + "\n\n")
    story_text.config(state=tk.DISABLED)
    story_text.yview(tk.END)

    if "THE END" in story_part:
        play_again()

# Function to handle the user's choice
def handle_choice():
    choice = entry.get().replace(' ', '_')  # Replace spaces with underscores
    entry.delete(0, tk.END)
    next_part = f"{choice.lower()}.txt"
    story_part = load_story_part(next_part)
    display_story_part(story_part)

# Function to start the game
def start_game(keyword=None):
    start_part = "beginning.txt" if not keyword else f"{keyword.lower()}.txt"
    story_part = load_story_part(start_part)
    display_story_part(story_part)

# Function to ask if the user wants to play again
def play_again():
    answer = simpledialog.askstring("Play Again", "Do you want to play again? (yes/no)")
    if answer and answer.lower() == 'yes':
        keyword = simpledialog.askstring("Keyword", "Enter a keyword to start from a specific part of the story (leave blank to start from the beginning):")
        story_text.config(state=tk.NORMAL)
        story_text.delete('1.0', tk.END)  # Clear the text box
        story_text.config(state=tk.DISABLED)
        start_game(keyword)
    else:
        root.quit()

# Main window setup
root = tk.Tk()
root.title("Choose Your Own Adventure Game")

# Scrolled text widget for story display
story_text = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
story_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry widget for user input
entry = tk.Entry(root)
entry.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
entry.bind("<Return>", lambda event: handle_choice())

# Check for keyword at the beginning
keyword = simpledialog.askstring("Keyword", "Enter a previous choice (i.e. 'left' or 'right') to start from a specific part of the story (leave blank to start from the beginning):")
start_game(keyword)

# Run the main loop
root.mainloop()
