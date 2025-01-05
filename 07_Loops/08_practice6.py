#start pattern

n=int(input("Enter n : "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1), end="")
    print("\n")

print("Pattern 2")

for i in range(1,n+1):
    print("*"*i,end="")
    print(" ")


print("Pattern 3")
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*"*1,end="")
        print(" "*(n-2),end="")
        print("*",end="")

    print(" ")
