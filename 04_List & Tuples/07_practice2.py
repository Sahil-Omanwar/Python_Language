#Write a programme to accept the mark of 7 students and display them in sorted manner
list=[]
a=int(input("Enter mark of student 1"))
list.append(a)

b=int(input("Enter mark of student 2"))
list.append(b)

c=int(input("Enter mark of student 3"))
list.append(c)

d=int(input("Enter mark of student 4"))
list.append(d)
e=int(input("Enter mark of student 5"))
list.append(e)

f=int(input("Enter mark of student 6"))
list.append(f)


print(list)

#sorted marks
list.sort()
print(list)

