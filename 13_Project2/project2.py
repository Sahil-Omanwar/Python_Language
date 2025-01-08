import random


n=random.randint(1,100)
a=-1
guess=0
while(a!=n):
    guess+=1
    a=int(input("Guess a number : "))
    if(a>n):
        print("Lower number pls")
    else:
        print("Higher number pls")

print(f"You have guessed the number correctly in {guess} attemps")