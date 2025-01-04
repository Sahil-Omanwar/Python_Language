#Write a program to find greates of 4 number entered by user


a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
c=int(input("Enter the c value"))
d=int(input("Enter the d value"))


e=max(a,b)
f=max(c,d)

if(e>f):
    print(f"Greatest number is{e}")
else:
    print(f"Greatest number if {f}")