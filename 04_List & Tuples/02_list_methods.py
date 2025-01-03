#List methods modify itself unlike string which produces new one

friends=["Sahil","Pranav","Humayun",7,True,44.50]

print("This is append method")
friends.append("Shubham")
print(friends )



print("This is reverse method")
friends.reverse()
print(friends )

print("This is insert method")
friends.insert(1,"Prem")
print(friends)


print("This is pop method")
friends.pop(1)
print(friends.pop(1))
print(friends )

print("This is remove method")
friends.remove(True)
print(friends)



list1=[3,5,3,52,5,623,6,7,2,4,0]
list2=["Sahil ","Pranav ","Humayun ","Prem","Shubham ","Shilavant"]
list1.sort()
list2.sort()
print(f"sorted list1 is:{list1}")
print(f"sorted list2 is:{list2}")

