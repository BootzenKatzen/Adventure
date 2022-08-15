import random #needed for random integers for LuckCheck

from time import sleep

def PZ():
    sleep(1.5)

def LuckCheck(): #flipping a coin for luck
    global coin
    flip = random.randint(0,1) #pulls either a 0 or 1 at random for coin flip
    if flip == 0:
        coin = "heads"
    elif flip == 1:
        coin = "tails"

def SPC(): #adding a quicker way to add line spaces
     print("")

def RM(): #adding a way to add a space and a pause
    PZ()
    SPC()

def print1(text): #prints with a pause so there's not a block of text all at once
    print(text)
    PZ()

def print2(text): #prints with a pause and a space to break up text
    print(text)
    RM()

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
    print2("This is the ADVENTURE ZONE!")
    global Adventurer #making variable global so it can be pulled into other parts of the code
    Adventurer = input("What is your name?\n").strip()
    RM()
    print("Hello %s!" %Adventurer)
    RM()

def Quest():
    while True:
        quest = input("Would you like to go on an Adventure? [Y/N]").lower().strip()
        if quest == "n":
            SPC()
            print2("Then why are you here?")
            print2("This is the adventure zone.")
            print2("The zone for adventures.")
            print2("You silly goose.")
            Leave()
        elif quest == "y":
            SPC()
            print("Well then, let's go", Adventurer,"!")
            RM()
            print2("I hope you have a wonderful time on your journey!")
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
    print1("...")
    print1("What? I don't understand.")
    print2("Try again")

def Sommelier():
    Hold()

def Crush():
    print2("Well, that wasn't the best idea.")
    print("He responds in kind, and crushes the bones in your hand.")
    print2("You pass out from the pain")
    print1("...")
    print1("...")
    print2("...")
    print1("You wake up to see a very attractive person standing over you")
    print1("They nurse you back to health, and you end up falling in love")
    print2("You get married and have 9 kids together")
    print2("You didn't really get to go on an adventure, but you live happily ever after anyway!")
    print2("THE END")
    Again()

def Weakling():
    print1("The viking seems dissappointed in your handshake")
    print1("... but he notices that you have very soft hands")
    print1("He shrugs and sits next to you to talk")
    print2("He introduces himself as Sven")
    print2("He buys you another round")
    print2("... and another")
    print2("... and another")
    print2("After several more rounds, some dancing, some laughing,\
and some drunken goat-tipping, you black out")
    print1("...")
    print1("...")
    print2("...")
    print1("You wake up with a raging headache, in an unfamiliar bed")
    print1("You smell bacon and eggs, and hear someone whistling in the kitchen")
    print2("You go to rub your eyes and notice a ring on your left hand")
    print2("You have married Sven after a night of drunken revelry")
    print1("He seems ecstatic to have you there")
    print2("He serves you a delicious breakfast in bed and kisses you on the forehead")
    print1("Breaking it off would break his poor heart")
    print1("And clearly he'd make a decent spouse")
    print2("So you decide to stay with him.")
    print2("You live happily ever after (?)")
    print2("THE END")
    Again()

def Listen():
    Hold()

def Rude():
    Hold()

def Party():
    print1("Sven grabs another chair for you")
    print1("He says'Hey,", Adventurer, "these are my pals, Jorgen, Ivan, and Dave ")
    print1("The three of them nod at you")
    print2("Sven asks'So what brings you here?'")
    print2("You tell them you were looking for a quest")
    print2("The 4 of them look at each other for a moment")
    print1("'We may have a job for you' says Jorgen")
    print1("'If you want it, that is' says Ivan")
    print2("Dave stays silent, but he nods")
    print("'Would you like to hear about it?' asks Sven")
    answer = input("[Y/N] ").lower().strip()
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
    print1("The viking is surprised, but delighted by your warrior etiquette")
    print1("He introduces himself as Sven Svenson")
    print2("He buys you another round, and invites you to his table")
    sit = input("Do you sit with him? [Y/N] ").lower().strip()
    if sit ==  "y":
        RM()
        Party()
    elif sit == "n":
        RM()
        Shy()


def BroShake():
    print1("You grasp the viking's hand firmly and give it a good shake")
    print2("He smiles at you in appreciation of your courtesy")
    print2("When you then try to swing into a bro hug, he is surprized but elated.")
    print2("(Little did you know, vikings in this world are big huggers)")
    print2("He releases your hand and goes for a full bear hug")
    print1("His arms wrap around your ribcage like iron bands")
    print()
    Again()

def DrinkingPal():
    print1("The viking in the corner also chugs his mead, and slams the mug on the table")
    print2("He approaches you")
    print2("He is larger than you thought, and you thought he was very large")
    print2("He holds out his hand to you.")
    print1("Do you:")
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
    print2("The bartender hands you a large mug of mead.")
    print2("The viking in the corner lifts his mug in salute.")
    print1("Do you:")
    print("A) Chug it")
    print("OR")
    print2("B) Sip it")
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
    print2("The bartender slides you a large frothy pint.")
    print1("Would you like to:")
    print("A) Sit at the bar")
    print("B)Find a table")
    print2("C) Stand awkwardly")
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
    print2("The bartender offers you three choices:")
    print1("Would you like:")
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
    print1("You enter the dimly lit tavern")
    print2("You see a lot of drunks")
    brawl = input("Would you like to start a fight? [Y/N]").lower().strip()
    if brawl == "y":
        RM()
        print1("That was a bad idea.")
        print1("There was a very large viking in the corner that you failed to notice.")
        print2("He bludgeons you in the head trying to stop the fight.")
        print2("But he is too strong for his own good.")
        print2("You died.")
        print("THE END")
        RM()
        Again()
    elif brawl == "n":
        RM()
        print2("Good choice, a very large, slightly grumpy viking was sitting in the corner.")
        Bar()
    else:
        SayAgain()
        SPC()
        Tavern()

def WakeUpCall():
    Hold()

def GoodLuck():
    print1("Nice call!")
    print2("You've got some good luck there!")
    WakeUpCall()

def Badluck(): #This will only show up the first time you fail the coin filp
    print1("Oh dear.")
    print2("What rotten luck.")
    print1("You lie there asleep deep in the meadow")
    print1("Sometimes you hear voices")
    print1("but no one comes close enough to find you.")
    print2("You slowly waste away, lost in dreams")
    print2("You died.")
    print2("THE END")
    print2("...")
    print1("Would you like to try your luck with coin flip again?")
    print2("(You'll keep the same call)")
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
    print1("Since it's a lovely day you decide to take a nap")
    print2("You lay down on a comfy patch, and the breeze lulls you to sleep")
    print2("...")
    print1("Unfortunately, this is a feild of magical poppies")
    print2("Once you fall asleep here you cannot wake up without external intervention")
    print1("Now it's all up to your luck")
    print1("We'll flip a coin!")
    RM()
    global call
    call = input("Heads or tails?").lower().strip()
    SPC()
    CoinFlip1()

def Botany():
    Hold()

def Woods():
    print1("The woods are very dark and dangerous")
    print1("You see an axe leaning against a tree by the start of the path")
    axe = input("Do you take it? [Y/N]")
    RM()
    print2("You enter the forest")
    print2("It is spooky, so you carefully creep along")
    print2("Suddenly you see a large gnarled bear in front of you!")
    bearfight = input("Do you dare to fight it? [Y/N]")
    if bearfight.lower().strip() == "y":
        if axe.lower().strip() == "y":
            RM()
            print1("With your axe at the ready, you pounce on the bear!")
            print2("It's a harrowing battle, but somehow you barely manage to win")
            print2("You take the bear's head as a tropy and head back to town, triumphant")
            print2("Congratulations on your first small but successful adventure!")
            Hold()
        elif axe.lower().strip() == "n":
            print2("Raring for adventure you leap into action!")
            print2("Unfortunately it's very hard to fight a bear barehanded")
            print2("If only you were 'bearhanded' instead.")
            print2("You died!")
            Print2("THE END")
            Again()
    elif bearfight.lower().strip() == "n":
        print1("You decide you'd rather not fight a bear on your own")
        print1("A very wise decision")
        print1("Perhaps you should go back to the tavern for reinforcements")
        Hold()

def Meadow():
    print1("The meadow is brightly lit, and full of flowers.")
    print1("There is a pleasant breeze blowing through.")
    print2("There doesn't appear to be anything dangerous nearby.")
    print1("Would you like to:")
    print("A) Take a nap")
    print("B) Examine the flowers")
    print("C) Decide to explore the woods instead")
    print2("D) Go back to the tavern")
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
    print1("Either you think it's too early to start drinking")
    print1("Or you're trying to avoid the stranger in a tavern cliche")
    print2("So you decide to explore outside instead")
    print1("You see:")
    print("A) A dark and spooky woods")
    print2("B) A bright and sunny meadow")
    explore = input("Where would you like to go?").lower().strip()
    if explore == "a":
        Woods()
    elif explore == "b":
        Meadow()

def choice1():
    print1("You are a young human, coming of age in a land of myth and magic")
    print1("You decide it's time to seek your fortune out in the world")
    print2("You leave your house, waving goodbye to your family.")
    print1("You start by following the path away from your home")
    print2("It leads into a small quaint town")
    print2("Smack dab in the middle of it is a large tavern")
    print2("Would you like to go into the tavern? [Y/N]")
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
