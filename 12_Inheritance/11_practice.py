#write a class complex to represent complex numbers along with overloaded operators + and *

class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self, other):
        return Complex(self.r + other.r,self.i+other.i)

    def __mul__(self, other):
        real_part=self.r+other.r-self.i*other.i
        img_part=self.r +c2.i+self.i*other.r

        return Complex(real_part,img_part)
    def __str__(self):
        return f"{self.r}+{self.i}i"

c1=Complex(1,2)
c2=Complex(3,4)
print(c1+c2)
print(c1*c2)

