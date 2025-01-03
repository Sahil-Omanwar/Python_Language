
friends=("Sahil","Pranav","Humayun",7,True,44.50)

a=friends.count(True)#Counts number of 2 in tuple
print(a)

b=friends.index("Pranav")#return the index of first occurance
print(b)

# c=friends.index("Omanwar")#return value error if no such element is present in tuple
# print(c)


print(len(friends))

#unpacking in tuple
tuple=(1,2,3)
a,b,c=tuple
print(a,b,c)

