#prime or not
n=int(input("Write  number : " ))

prime=True
for i in range(2,int(n/2)+1):
    if(n%i==0):

        prime=False

if prime==True:
    print("Number is a prime number")
else:
    print("Number is not a prime number")



