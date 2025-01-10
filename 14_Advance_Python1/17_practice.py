#write a list comprehension to print la list which contains the multiplication tabl,e of a user entered number

n=int(input("Enter the number : "))

table=[n*i for i in range(1,11)]
print(table)