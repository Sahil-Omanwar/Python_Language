#Factorial using for loop

n=int(input("Write  number : " ))
fact=1
for i in range(1,n+1):
    fact*=i

print(f"Factorial of {n} is {fact}")