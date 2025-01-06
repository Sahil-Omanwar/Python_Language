#print pattern using funtion

n=int(input("Enter the value of n : "))

def pattern(n):
    for i in range(1,n+1):
        print("*"*(n-i+1),end="")
        print(" ")

pattern(n)