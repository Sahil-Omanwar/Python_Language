from math import factorial

n=int(input("Provide input for your problem : "))

def factorial(n):
    if n==1 or n==0:
        return 1
    
    a=n*factorial(n-1)
    return a

a=factorial(n)
print(f"factorial of {n} is :{a}")
