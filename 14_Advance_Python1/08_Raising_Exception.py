a=int(input("Enter first number :"))
b=int(input("Enter second number :"))

if(b==0):
    raise ZeroDivisionError("Programme is not meant to be divided by zero")
else:
    print(f"Division is : {a/b}")