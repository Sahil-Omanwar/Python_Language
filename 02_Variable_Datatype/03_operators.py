"""
1)Arithmetic:+,-,*,/
2)Assignment:=,+=,-=
3)Comparison:==,>,>=,<,!=
4)Logical operators:and,or,not
"""
from win32gui import FlashWindowEx

#Arithmetic operator
print("Arithmetic operators ")
a=30
b=20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#Assignment operators
print("Assignment operators")
c=4-2 #Assign 4-2 in c
c-=2
print(c)
d=6
d+=3#increment the value of d by 3 and then assign this value to d
print(d)
e=5
e*=5
print(e)
f=10
e/=2
print(e)

#Comparison operator{return type is always boolean
print("Comparison operators")
a=10
b=20
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a!=b)
print(a==b)

#Logical operators
print("Logical operators")

a=True or False
print(a)
b=True and True
print(b)
c=True and False
print(c)
d=False or True
print(d)
e=not False
print(e)
f=not True
print(f)