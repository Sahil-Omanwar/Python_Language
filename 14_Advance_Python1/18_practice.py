#write a programme to display a/b where a and b are integer.If b=0,display infinite by handling zero Divivsion error
try:
   a=int(input("Enter first number : "))
   b=int(input("Enter second number : "))
   print(a/b)
except ZeroDivisionError as ze:
    print("infinite")