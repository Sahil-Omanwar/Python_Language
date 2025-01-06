#recursive function to find sum of n number

n=int(input("Enter the number : "))

def summation(n,sum=0):
    if n==0:
        return 0
    sum=sum+n+summation(n-1)
    return sum

ans=summation(10)
print(f"summation of {n} numbers is : {ans}")

