#Calculate the grade


n=int(input("Enter the grade of student : "))

if(n<100 and n>=90):
    print("Grade is : Ex")
elif(n<90 and n>=80):
    print("Grade is : A")
elif(n<80 and n>=70):
    print("Grade is B")
elif(n<70 and n>=60):
    print("Grade is C")
elif(n<60 and n>=50):
    print("Grade is D")
else:
    print("Grade is : F")