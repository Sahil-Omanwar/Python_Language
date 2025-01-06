
list1=["Harry","Rohan","Shubham","an"]


def delete1(l,word):
     n=[]
     for item in l:
         if not(item==word):
             n.append(item.strip(word))
     return n

print(delete1(list1,"an"))