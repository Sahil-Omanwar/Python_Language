#sum of first n natutal numbers using while

n=int(input("Write  number : " ))

sum=0
i=0
while i<n+1:
    sum+=i
    i+=1

print(f"Sum of first {n} natural numbers is :{sum}")