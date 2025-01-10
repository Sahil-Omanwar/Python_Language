#filter a list of numbers which are divisible by 5

l=[1,2,3,4,5,66,7,8,5,40,45]

def div_5(i):

        if(i%5==0):
            return True
        else:
            return False


ans=filter(div_5,l)
print(list(ans))