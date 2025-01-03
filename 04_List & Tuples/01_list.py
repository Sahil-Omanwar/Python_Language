#list can store any type of data in it

friends=["Sahil","Pranav","Humayun",7,True,44.50]
#All type of data be it string,int.float,boolean in list

#Accessing members :Done using indexes

print(friends[0][:3])
friends[0]="Sahil Omanwar" #Lists are mutable
print(friends)

friends[3]=friends[0][0:6]
print(friends)


#Slicing in list
true_friend=friends[0:3]
print(true_friend)
