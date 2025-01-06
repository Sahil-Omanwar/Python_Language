#Functions with arguments

def good_day(name,ending):
    print("Good day",name)
    print(ending)

good_day("sahil","Kaise ho")


#return value

def suma(a,b):
    return a+b

a=suma(10,1000)
print(a)

#default valuee concept
def good_boy(name,ending="You are good boy"):
    print(f"Hi {name} ,{ending}")

good_boy("Sahil")
good_boy("Sam","You are bad boy ")