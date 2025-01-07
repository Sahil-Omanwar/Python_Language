# #game() function in programme lets use play a game and return the score as int
# read a file Hi-score.txt which is either blank ot contains previous high score update if new is bigger


import random
def game():
    print("You are playing game")
    score=random.randint(1,62)
    with open("Hi-score.txt") as f:
        hiScore=f.read()
        if(hiScore!=""):
            hiScore=int(hiScore)
        else:
            hiScore=0

    print(f"Your score is : {score}")

    if(score>hiScore):
          with open("Hi-score.txt","w") as f:
              f.write(str(score))


    return score

game()



