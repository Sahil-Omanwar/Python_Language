#if ,elif,else are conditions used in python
##When  we want to execute instructions on a conditions being met

age=int(input("Enter you age"))

##USE OF IF-ELSE
if (age>=18):
     print("You are adult and can vote")
else:
    print("You are invalid to vote")



##USE OF IF-ELIF-ELSE LADDER
if(age<0 or age>120):
    print("Invalid age ")
elif(age>=18):
    print("You can vote")
else:
    print("You cannot vote")

#print yes if age of user greater than 18
if(age>=18):
    print("yes")
else:
    print("No")