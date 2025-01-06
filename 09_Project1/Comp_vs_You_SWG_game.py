
import random
numbers=[-1,1,0]
computer=random.choice(numbers)
user=input("what do you want to choose ")
choice_dict={
    "Snake":1,
    "Water":-1,
    "Gun":0
}

reverse_dict={
    1:"Snake",
    -1:"Water",
    0:"Gun"
}
user1=choice_dict[user]
if(computer==user1):
    print("Its a draw")
else:
    if(computer==-1 and user1==1):
        print("You win")
    elif(computer==-1 and user1==0):
        print("You loose")
    elif(computer==1 and user1==-1):
        print("you loose")
    elif(computer==1 and user1==0):
        print("You win")
    elif(computer==0 and user1==-1):
        print("You win")
    elif(computer==0 and user1==1):
        print("You loose")
    else:
        print("Something went wrong")

print(f"Computer choosed {reverse_dict[computer]}")