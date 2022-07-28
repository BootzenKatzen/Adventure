def start_game():
    print("This is the ADVENTURE ZONE!")
    print("")
    Adventurer = input("What is your name?")
    print("")
    print("Hello", Adventurer,"!")


def again():
    again = input("Would you like to play again?")
    if again.lower().strip() == "y":
        game()
    else:
        print("Okay, bye!")

def SayAgain():
    print("...")
    print("What? I don't understand")
    print("")


def the_beginning():
        while True:
            quest = input("Would you like to go on a quest? [Y/N]")
            if quest.lower().strip() == "n":
                print("")
                print("Then why are you here?")
                print("")
                continue
            elif quest.lower().strip() =="y":
                print("")
                print("Welcome Adventurer!")
            else:
                SayAgain()
                continue
            return
def Mead():
    print("Placeholder")

def Ale():
    print("Placeholder")

def Milk():
    print("Placeholder")

def Drinks():
    print("The bartender offers you three choices:")
    print("A) Mead")
    print("B) Ale")
    print("C) Milk")
    drank = input("Which do you choose? [A/B/C]")
    if drank.lower().strip() == "a":
        Mead()
    elif drank.lower().strip() == "b":
        Ale()
    elif drank.lower().strip() == "c":
        Milk()
    else:
        SayAgain()
        Drinks()

def Sober():
    print("Placeholder")

def Bar():
    drink = input("Would you like to get a drink? [Y/N]")
    if drink.lower().strip() == 'y':
        Drinks()
    elif drink.lower().strip() == "n":
        Sober()
    else:
        SayAgain()
        Bar()

def Tavern():
    brawl = input("Would you like to start a fight? [Y/N]")
    if brawl.lower().strip() == "y":
        print("That was a bad idea.")
        print("A Viking bludgeons you in the head and you die.")
        print("")
        print("THE END")
        again()
    elif brawl.lower().strip() == "n":
        print("Good choice, the viking in the corner looked angry")
        Bar()
    else:
        SayAgain()
        Tavern()
def Woods():
    print("Placeholder")

def Meadow():
    print("Placeholder")

def Outdoors():
    explore = input("Where would you like to go?")
    if explore.lower().strip() == "a":
        Woods()
    elif explore.lower().strip() == "b":
        Meadow()


def choice1():
    tavern = input("Would you like to go into the tavern? [Y/N]")
    if tavern.lower().strip() == "y":
        print("You enter the dimly lit tavern")
        print("You see a lot of drunks")
        Tavern()
    elif tavern.lower().strip() == "n":
        print("You decide to explore outside instead")
        print("You see:")
        print("A) A dark and spooky woods")
        print("B) A bright and sunny meadow")
        Outdoors()

def game():
    the_beginning()
    choice1()

def start1():
    start_game()
    game()

start1()
