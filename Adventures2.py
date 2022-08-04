import random #needed for random integers for LuckCheck

from time import sleep

def PZ():
    sleep(2)

def LuckCheck(): #flipping a coin for luck
    global coin
    flip = random.randint(0,1) #pulls either a 0 or 1 at random for coin flip
    if flip == 0:
        coin = "heads"
    elif flip == 1:
        coin = "tails"

def SPC(): #adding a quicker way to add line spaces
     print("")

def RM():
    PZ()
    SPC()

def Leave(): #adding a way out of the game
    leave = input("Would you like to leave? [Y/N]").lower().strip()
    if leave == "y":
        RM()
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
            RM()
            print("This is the adventure zone.")
            RM()
            print("The zone for adventures.")
            RM()
            print("You silly goose.")
            SPC()
            Leave()
        elif quest == "y":
            SPC()
            print("Well then, let's go", Adventurer,"!")
            print("I hope you have a wonderful time on your journey!")
            RM()
            SPC()
            break
        else:
            SayAgain()
            continue

def Again(): #quick way to restart after an ending
    again = input("Would you like to adventure again? [Y/N]").lower().strip()
    if again == "y":
        RM()
        game()
    elif again == "n":
        RM()
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
    PZ()
    print("What? I don't understand.")
    PZ()
    print("Try again")

def Sommelier():
    Hold()

def Crush():
    print("Well, that wasn't the best idea.")
    RM()
    print("He responds in kind, and crushes the bones in your hand.")
    print("You pass out from the pain")
    RM()
    print("...")
    PZ()
    print("...")
    PZ()
    print("...")
    RM()
    print("You wake up to see a very attractive person standing over you")
    PZ()
    print("They nurse you back to health, and you end up falling in love")
    PZ()
    print("You get married and have 9 kids together")
    RM()
    print("You didn't really get to go on an adventure, but you live happily ever after anyway!")
    RM()
    print("THE END")

def Weakling():
    print("The viking seems dissappointed in your handshake")
    PZ()
    print("... but he notices that you have very soft hands")
    PZ()
    print("He shrugs and sits next to you to talk")
    PZ()
    print("He buys you a round")
    RM()
    print("... and another")
    RM()
    print("... and another")
    RM()
    print("After several more rounds, some dancing, some lauging, and some drunken goat-tipping, you black out")
    RM()
    print("...")
    PZ()
    print("...")
    PZ()
    print("...")
    RM()
    print("You wake up with a raging headache, in an unfamiliar bed")
    PZ()
    print("You smell bacon and eggs, and hear someone whistling in the kitchen")
    PZ()
    print("You go to rub your eyes and notice a ring on your left hand")
    PZ()
    print("You have married the viking after a night of drunken revelry")
    RM()
    print("You live happily ever after (?)")
    RM()
    print("THE END")
    RM()
    print("(For now)")
    RM()
    Again()

def Listen():
    Hold()

def Rude():
    Hold()

def Party():
    print("Sven grabs another chair for you")
    PZ()
    print("He says'Hey,", Adventurer, "these are my pals, Jorgen, Ivan, and Dave ")
    PZ()
    print("The three of them nod at you")
    PZ()
    print("Sven asks'So what brings you here?'")
    PZ()
    print("You tell them you were looking for a quest")
    RM()
    print("The 4 of them look at each other for a moment")
    RM()
    print("'We may have a job for you' says Jorgen")
    PZ()
    print("'If you want it, that is' says Ivan")
    PZ()
    print("Dave stays silent, but he nods")
    RM()
    print("'Would you like to hear about it?' asks Sven")
    answer = input("Y/N").lower().strip()
    SPC()
    if answer == "y":
        RM()
        Listen()
    elif answer == "n":
        RM()
        Rude()

def Shy():
    Hold()

def GoodShake():
    print("The viking is surprised, but delighted by your warrior etiquette")
    PZ()
    print("He introduces himself as Sven Svenson")
    PZ()
    print("He buys you another round, and invites you to his table")
    RM()
    sit = input("Do you sit with him? [Y/N]").lower().strip()
    if sit ==  "y":
        RM()
        Party()
    elif sit == "n":
        RM()
        Shy()


def BroShake():
    Hold()

def DrinkingPal():
    print("The viking in the corner also chugs his mead, and slams the mug on the table")
    PZ()
    print("He approaches you")
    PZ()
    print("He is larger than you thought, and you thought he was very large")
    RM()
    print("He holds out his hand to you.  Do you:")
    RM()
    print("A)Grab his hand as hard as you can")
    print("B)Give him the limp fish handshake")
    print("C)Grab his forearm")
    print("D)Give a firm handshake and try for the bro hug")
    shake = input().lower().strip()
    if shake == "a":
        RM()
        Crush()
    elif shake == "b":
        RM()
        Weakling()
    elif shake == "c":
        RM()
        GoodShake()
    elif shake == "d":
        RM()
        BroShake()
    else:
        RM()
        DrinkingPal()


def Mead():
    print("The bartender hands you a large mug of mead.")
    RM()
    print("The viking in the corner lifts his mug in salute.")
    RM()
    print("Do you:")
    print("A) Chug it")
    print("OR")
    print("B) Sip it")
    SPC()
    chug = input().lower().strip()
    if chug == "a":
        RM()
        DrinkingPal()
    elif chug == "b":
        RM()
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
        RM()
        Stool()
    elif takeaseat == "b":
        RM()
        Table()
    elif takeaseat == "c":
        RM()
        Awkward()
    else:
        SayAgain()
        Ale()

def Milk():
    Hold()

def Drinks():
    print("The bartender offers you three choices:")
    RM()
    print("Would you like:")
    print("A) Mead")
    print("B) Ale")
    print("C) Milk")
    drank = input().lower().strip()
    if drank == "a":
        RM()
        Mead()
    elif drank == "b":
        RM()
        Ale()
    elif drank == "c":
        RM()
        Milk()
    else:
        SayAgain()
        Drinks()

def Sober():
    Hold()

def Bar():
    drink = input("Would you like to get a drink? [Y/N]").lower().strip()
    if drink == 'y':
        RM()
        Drinks()
    elif drink == "n":
        RM()
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
        RM()
        print("That was a bad idea.")
        print("There was a very large viking in the corner that you failed to notice.")
        print("He bludgeons you in the head trying to stop the fight.")
        RM()
        print("But he is too strong for his own good.")
        RM()
        print("You died.")
        SPC()
        print("THE END")
        RM()
        Print("(For now)")
        RM()
        Again()
    elif brawl == "n":
        RM()
        print("Good choice, a very large, slightly grumpy viking was sitting in the corner.")
        RM()
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
    RM()
    WakeUpCall()

def Badluck(): #This will only show up the first time you fail the coin filp
    print("Oh dear.")
    print("What rotten luck.")
    RM()
    print("You lie there asleep deep in the meadow")
    print("Sometimes you hear voices")
    print("but no one comes close enough to find you.")
    print("You slowly waste away, lost in dreams")
    RM()
    print("You died.")
    RM()
    print("THE END")
    RM("(For now)")
    RM()
    print("...")
    SPC()
    print("Would you like to try your luck with coin flip again?")
    print()"(You'll keep the same call)")
    SPC()
    AnotherFlip()

def AnotherFlip(): #so they can try their luck again without going through the whole adventure
    flipagain = input().lower().strip()
    if flipagain == "y":
        RM()
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
        RM()
        AnotherFlip()

def CoinFlip1(): #initial coin flip leading to good or bad end
    LuckCheck()
    print("You called ", call, "and it came up ", coin)
    if coin == call:
        RM()
        GoodLuck()
    else:
        RM()
        Badluck()

def Nap():
    print("Since it's a lovely day you decide to take a nap")
    print("You lay down on a comfy patch, and the breeze lulls you to sleep")
    RM()
    print("...")
    RM()
    print("Unfortunately, this is a feild of magical poppies")
    print("Once you fall asleep here you cannot wake up without external intervention")
    RM()
    print("Now it's all up to your luck")
    print("We'll flip a coin!")
    RM()
    global call
    call = input("Heads or tails?").lower().strip()
    SPC()
    CoinFlip1()

def Botany():
    Hold()

def Woods():
    print("The woods are very dark and dangerous")
    PZ()
    print("You see an axe leaning against a tree by the start of the path")
    PZ()
    axe = input("Do you take it?")
    RM()
    print("You enter the forest")
    RM()
    print("It is spooky, so you creep along")
    RM()
    print("Suddenly you see a large gnarled bear in front of you!")
    bearfight = input("Do you dare to fight it?")
    if bearfight.lower().strip() == "y" or "yes":
        if axe.lower().strip() == "y" or "yes":
            RM()
            print("With your axe at the ready, you pounce on the bear!")
            PZ()
            print("It's a harrowing battle, but somehow you barely manage to win")
            PZ()
            print("You take the bear's head as a tropy and head back to town, triumphant")
            RM()
            print("Congratulations on your first small but successful adventure!")
            Hold()
        elif axe.lower().strip() == "n" or "no":
            print("Raring for adventure you leap into action!")
            PZ()
            print("Unfortunately it's very hard to fight a bear barehanded")
            RM()
            print("If only you were 'bearhanded' instead.")
            RM()
            print("You died!")
            RM()
            Print("THE END")
            RM()
            Print("(For now)")
            RM()
            Again()
    elif bearfight.lower().strip() == "n" or "no":
        print("You decide you'd rather not fight a bear on your own")
        print("A very wise decision")
        print("Perhaps you should go back to the tavern for reinforcements")
        Hold()

def Meadow():
    print("The meadow is brightly lit, and full of flowers.")
    PZ()
    print("There is a pleasant breeze blowing through.")
    PZ()
    print("There doesn't appear to be anything dangerous nearby.")
    RM()
    print("Would you like to:")
    print("A) Take a nap")
    print("B) Examine the flowers")
    print("C) Decide to explore the woods instead")
    print("D) Go back to the tavern")
    SPC()
    flowerchild = input().lower().strip()
    if flowerchild == "a":
        RM()
        Nap()
    elif flowerchild == "b":
        RM()
        Botany()
    elif flowerchild == "c":
        RM()
        Woods()
    elif flowerchild == "d":
        RM()
        Tavern()
    else:
        SayAgain()
        Meadow()

def Outdoors():
    print("Either you think it's too early to start drinking")
    PZ()
    print("Or you're trying to avoid the stranger in a tavern cliche")
    PZ()
    print("So you decide to explore outside instead")
    RM()
    print("You see:")
    print("A) A dark and spooky woods")
    print("B) A bright and sunny meadow")
    RM()
    explore = input("Where would you like to go?").lower().strip()
    if explore == "a":
        Woods()
    elif explore == "b":
        Meadow()

def choice1():
    print("You are a young human, coming of age in a land of myth and magic")
    PZ()
    print("You decide it's time to seek your fortune out in the world")
    PZ()
    print("You leave your house, waving goodbye to your family.")
    RM()
    print("You start by following the path away from your home")
    print("It leads into a small quaint town")
    RM()
    print("Smack dab in the middle of it is a large tavern")
    SPC()
    print("Would you like to go into the tavern? [Y/N]")
    SPC()
    tavern = input().lower().strip()
    if tavern == "y":
        RM()
        Tavern()
    elif tavern == "n":
        RM()
        Outdoors()

def game():
    choice1()

def start1():
    start_game()
    Quest()
    game()

start1()
