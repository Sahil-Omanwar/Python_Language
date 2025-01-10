#programme to find maximum in a list

from functools import reduce
l=[66,4,2,6,8,3,7,9,34]

def maxi(a,b):
    if a>b:
        return a
    else:
        return b

ans=reduce(maxi,l)
print(ans)