#print the table

n=int(input("Write a table for which number : " ))
#Using for loop
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

#using while loop
i=1
while(i<11):
    print(f"{n}*{i}={n*i}")
    i+=1
