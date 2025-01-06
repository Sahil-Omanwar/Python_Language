#snake vs water=snake wins by drinking water
#water vs gun:water wins as gun gets drown in water
#gun vs snake :gun wins by shooting snake
#draw:If both chooses same object


a=input("What do you want to choose A : ")
b=input("What do you want to choose B: ")

wins = ""
def output(a,b):

    if(a=="Snake"):
        if(b=="Water"):
            wins=f"a with {a} has won the game {b}"
        elif(b=="Gun"):
            wins=f"b with {b} has won the game {a}"
        else:
            wins="Draw"
    elif(a=="Gun"):
        if(b=="Snake"):
            wins=f"a with {a} has won the game {b}"

        elif(b=="Water"):
            wins=f"b with {b} has won the game {a}"
        else:
            wins="Draw"
    else:
        if(b=="Snake"):
            wins=f"b with {b} has won the game over {a}"
        elif(b=="Gun"):
            wins=f"a with {a} has won the game over {b}"
        else:
            wins="Draw"

    return wins



if(output(a,b)=="Draw"):
    print(f"The game is has been resulted in draw with both stating {a}")
else:
    print(f"{output(a,b)} ")