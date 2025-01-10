#write a programe to print 3rd,5th and seventh element from a list using enumerate

l=[1,2,3,4,5,6,7,8,9]

for index,i in enumerate(l):
    if(index==2 or index ==4 or index==6):
        print(f'{index+1}:{i}')