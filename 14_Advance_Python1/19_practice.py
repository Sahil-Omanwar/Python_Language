#store multiplication table generated in problem 3 in  afile named tables.txt
n=int(input("Enter a number : "))
table=[n*i for i in range(1,11)]

with open("Tables.txt","a") as f1:
     f1.write(f"Table of {n} :{str(table)}\n")



