#program using function to find greatest of 2 number


a=int(input("Enter first number :"))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

def greatest(a,b,c):
    d=max(a,b)
    e=max(d,c)
    return e

ans=greatest(a,b,c)
print(f"Greatest of {a},{b},{c} is : {ans}")