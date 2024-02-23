
def choice1(event=None):  # first choice - used for testing GUI function
    ui_text()  # will print the user input after button click
    whereto = uip_low()  # uses lowercase version of input for variable
    empty()  # empties entry widget
    if whereto == "woods":
        # This will have descriptions of the next event
        # as well as the next choice to be made
        quest("The woods are spooky")
        change_cmd(woods)
        # changes button command to the next event
        # so it's prepared to recieve the next input
    elif whereto == "tavern":
        add_text1("The tavern is crowded")
        # same as "woods" but going to a different event
        change_cmd(tavern)
    else:
        what()
        # in case the us
