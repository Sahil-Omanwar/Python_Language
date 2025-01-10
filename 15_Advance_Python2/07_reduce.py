l=[1,2,3,4,5]
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum,l))