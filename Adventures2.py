import random #needed for random integers for LuckCheck

def LuckCheck(): #flipping a coin for luck
    global coin
    flip = random.randint(0,1) #pulls either a 0 or 1 at random for coin flip
    if flip == 0:
        coin = "heads"
    elif flip == 1:
        coin = "tails"

def SPC(): #adding a quicker way to add line spaces
     print("")

def Leave(): #adding a way out of the game
    leave = input("Would you like to leave? [Y/N]").lower().strip()
    if leave == "y":
        print("Goodbye!")
        quit()
    elif leave == "n":
        Quest()
    else:
        SayAgain()
        Leave()

def start_game(): #Welcome screen
    print("This is the ADVENTURE ZONE!")
    SPC()
    global Adventurer #making variable global so it can be pulled into other parts of the code
    Adventurer = input("What is your name?\n")
    SPC()
    print("Hello", Adventurer,"!")
    SPC()

def Quest():
    while True:
        quest = input("Would you like to go on an Adventure? [Y/N]").lower().strip()
        if quest == "n":
            SPC()
            print("Then why are you here?")
            SPC()
            print("This is the adventure zone.")
            SPC()
            print("The zone for adventures.")
            SPC()
            print("You silly goose.")
            SPC()
            Leave()
        elif quest == "y":
            SPC()
            print("Well then, let's go", Adventurer,"!")
            print("I hope you have a wonderful time on your journey!")
            SPC()
            SPC()
            break
        else:
            SayAgain()
            continue

def Again(): #quick way to restart after an ending
    again = input("Would you like to adventure again? [Y/N]").lower().strip()
    if again == "y":
        game()
    elif again == "n":
        print("Okay, bye!")
        quit()
    else:
        SayAgain()
        Again()

def Hold(): #adding a quick way to add a placeholder for playtesting
    print("Placeholder")
    Again()

def SayAgain(): #keeps loops from breaking if player makes a typo
    print("...")
    print("What? I don't understand.")
    print("Try again")

def Sommelier():
    Hold()

def Crush():
    Hold()

def Weakling():
    Hold()

def GoodShake():
    Hold()

def BroShake():
    Hold()

def DrinkingPal():
    print("The viking in the corner also chugs his mead, and slams the mug on the table")
    print("He approaches you")
    print("He is larger than you thought, and you thought he was very large")
    SPC()
    print("He holds out his hand to you.  Do you:")
    SPC()
    print("A)Grab his hand as hard as you can")
    print("B)Give him the limp fish handshake")
    print("C)Grab his forearm")
    print("D)Give a firm handshake and try for the bro hug")
    shake = input().lower().strip()
    if shake == "a":
        SPC()
        Crush()
    elif shake == "b":
        SPC()
        Weakling()
    elif shake == "c":
        SPC()
        GoodShake()
    elif shake == "d":
        SPC()
        BroShake()
    else:
        SPC()
        SayAgain()
        DrinkingPal()


def Mead():
    print("The bartender hands you a large mug of mead.")
    SPC()
    print("The viking in the corner lifts his mug in salute.")
    SPC()
    print("Do you:")
    print("A) Chug it")
    print("OR")
    print("B) Sip it")
    SPC()
    chug = input().lower().strip()
    if chug == "a":
        DrinkingPal()
    elif chug == "b":
        Sommelier()
    else:
        SayAgain()
        Mead()

def Stool():
    Hold()

def Table():
    Hold()

def Awkward():
    Hold()

def Ale():
    print("The bartender slides you a large frothy pint.")
    print("Would you like to:")
    print("A) Sit at the bar")
    print("B)Find a table")
    print("C) Stand awkwardly")
    SPC()
    takeaseat = input().lower().strip()
    if takeaseat == "a":
        Stool()
    elif takeaseat == "b":
        Table()
    elif takeaseat == "c":
        Awkward()
    else:
        SayAgain()
        Ale()

def Milk():
    Hold()

def Drinks():
    print("The bartender offers you three choices:")
    SPC()
    print("Would you like:")
    print("A) Mead")
    print("B) Ale")
    print("C) Milk")
    drank = input().lower().strip()
    if drank == "a":
        SPC()
        Mead()
    elif drank == "b":
        SPC()
        Ale()
    elif drank == "c":
        SPC()
        Milk()
    else:
        SayAgain()
        Drinks()

def Sober():
    Hold()

def Bar():
    drink = input("Would you like to get a drink? [Y/N]").lower().strip()
    if drink == 'y':
        SPC()
        Drinks()
    elif drink == "n":
        SPC()
        Sober()
    else:
        SayAgain()
        Bar()

def Tavern():
    print("You enter the dimly lit tavern")
    print("You see a lot of drunks")
    SPC()
    brawl = input("Would you like to start a fight? [Y/N]").lower().strip()
    if brawl == "y":
        print("BAD END 1:")
        SPC()
        print("That was a bad idea.")
        print("There was a very large viking in the corner that you failed to notice.")
        print("He bludgeons you in the head trying to stop the fight.")
        SPC()
        print("But he is too strong for his own good.")
        SPC()
        print("You died.")
        SPC()
        print("THE END")
        SPC()
        Again()
    elif brawl == "n":
        SPC()
        print("Good choice, a very large, slightly grumpy viking was sitting in the corner.")
        SPC()
        Bar()
    else:
        SayAgain()
        SPC()
        Tavern()

def WakeUpCall():
    Hold()

def GoodLuck():
    print("Nice call!")
    print("You've got some good luck there!")
    WakeUpCall()

def Badluck(): #This will only show up the first time you fail the coin filp
    print("Oh dear.")
    print("What rotten luck.")
    SPC()
    SPC()
    print("BAD END 2:")
    SPC()
    print("You lie there asleep deep in the meadow")
    print("Sometimes you hear voices")
    print("but no one comes close enough to find you.")
    print("You slowly waste away, lost in dreams")
    SPC()
    print("You died.")
    SPC()
    print("...")
    SPC()
    print("Would you like to try the coin flip again? (You'll keep the same call)")
    SPC()
    AnotherFlip()

def AnotherFlip(): #so they can try their luck again without going through the whole adventure
    flipagain = input().lower().strip()
    if flipagain == "y":
        CoinFlip2()
    else:
        print("Maybe next time, huh?")
        SPC()
        Again()

def CoinFlip2(): #so it doesn't give the whole "BAD END" a second time
    LuckCheck()
    print("You called ", call, "and it came up ", coin)
    if coin == call:
        GoodLuck()
    else:
        print("Bad luck again?")
        print("Drat.")
        print("Want another flip?")
        AnotherFlip()

def CoinFlip1(): #initial coin flip leading to good or bad end
    LuckCheck()
    print("You called ", call, "and it came up ", coin)
    if coin == call:
        SPC()
        GoodLuck()
    else:
        SPC()
        Badluck()

def Nap():
    print("Since it's a lovely day you decide to take a nap")
    print("You lay down on a comfy patch, and the breeze lulls you to sleep")
    SPC()
    print("...")
    SPC()
    print("Unfortunately, this is a feild of magical poppies")
    print("Once you fall asleep here you cannot wake up without external intervention")
    SPC()
    print("Now it's all up to your luck")
    print("We'll flip a coin!")
    SPC()
    global call
    call = input("Heads or tails?").lower().strip()
    SPC()
    CoinFlip1()

def Botany():
    Hold()

def Woods():
    Hold()

def Meadow():
    print("The meadow is brightly lit, and full of flowers.")
    print("There is a pleasant breeze blowing through.")
    print("There doesn't appear to be anything dangerous nearby.")
    SPC()
    print("Would you like to:")
    print("A) Take a nap")
    print("B) Examine the flowers")
    print("C) Decide to explore the woods instead")
    print("D) Go back to the tavern")
    SPC()
    flowerchild = input().lower().strip()
    if flowerchild == "a":
        SPC()
        Nap()
    elif flowerchild == "b":
        SPC()
        Botany()
    elif flowerchild == "c":
        Woods()
    elif flowerchild == "d":
        Tavern()
    else:
        SayAgain()
        Meadow()

def Outdoors():
    print("Either you think it's too early to start drinking")
    print("Or you're trying to avoid the stranger in a tavern cliche")
    print("So you decide to explore outside instead")
    SPC()
    print("You see:")
    print("A) A dark and spooky woods")
    print("B) A bright and sunny meadow")
    SPC()
    explore = input("Where would you like to go?").lower().strip()
    if explore == "a":
        Woods()
    elif explore == "b":
        Meadow()

def choice1():
    print("You are a young human, coming of age in a land of myth and magic")
    print("You decide it's time to seek your fortune out in the world")
    print("You leave your house, waving goodbye to your family.")
    SPC()
    print("You start by following the path away from your home")
    print("It leads into a small quaint town")
    SPC()
    print("Smack dab in the middle of it is a large tavern")
    SPC()
    print("Would you like to go into the tavern? [Y/N]")
    SPC()
    tavern = input().lower().strip()
    if tavern == "y":
        SPC()
        Tavern()
    elif tavern == "n":
        SPC()
        Outdoors()

def game():
    choice1()

def start1():
    start_game()
    Quest()
    game()

start1()
