#proof of concept that I can create bookmarks so people can jump to a specific part of the story.


def choice1(text):
    if text == "": #if text is empty - ie it was called as choice1() it acts like the normal choice and asks for InPut
        variable = input("Woods or tavern?").lower().strip()
    else:
        variable = text
    if variable == "woods":
        print("the woods are spooky")
    elif variable == "tavern":
        print("the tavern is crowded")
    else:
        print("What?")
        choice1()

def game():
    print("Welcome!")
    print()
    jumpstart = input("Would you like to start from a bookmark?").lower().strip()
    if jumpstart == "y":
        bookmark = input("What is the bookmark's keyword?").lower().strip()
        if bookmark == "choice2":
            choice1("woods") #woods is the bookmark that would take it to the next choice - needs to be in quotes or it won't work
        else:
            "Huh?"
            game()
    elif jumpstsart == "n":
        print("Ok, lets start at the beginning!")
        choice1()

game()
