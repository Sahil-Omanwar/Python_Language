#add

s={1,2,3,412,435,14,57,53}
s.add(999)
print((s))

print(len(s))

s.remove(3)
print(s)

s.pop()#randomly deletes 1 element from set
print(s)

s.clear()#clears all the set
print(s)

s1={1,3,5,7,3,6}
s2={1,2,4,7,8,9}
print(s1.union(s2))
print(s1.intersection(s2))
print((s1.difference(s2)))
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
print(s2.issuperset(s1))