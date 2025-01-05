#used to do repetative task


#FOR LOOP
for i in range(1,6):
    print(i)

for i in range(6):
    print(i)

#with stepsize
for i in range(10,100,4):
    print(i)

#For loop with string
t=(2,3,5,6,7)
for i in t:
    print(i)

#For loop with string
name="Sahil"
for i in name:
    print(i)

#Foor loop with else
list1=[0,1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i%2==0:
        print(f"{i} is divisible by 2")
    else:
        print(f"{i} is not divisible by 2")


#Break with loop
print("Break with loops")
for i in range(10):
    if(i==5):
        break
    else:
        print(i)

#Continue with loop
print("Break with loop  ")
for i in range(10):
    if(i==5):
        continue
    else:
        print(i)

#Pass
#it states to do nothing
for i in range(200):
    pass