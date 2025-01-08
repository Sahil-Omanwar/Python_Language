#class calculator capable of finding square ,cube and square root of a number
#add a static method to greet user
import math


class Calculator:

    def __init__(self,n):
        self.n=n

    def square(self):
        ans=self.n * self.n
        print(f"Square of a number is : {ans}")
    def cube(self):
        ans=self.n * self.n * self.n
        print(f"Cube of a number is : {ans}")
    def square_root(self):
        ans=math.sqrt(self.n)
        print(F"Square Root of a number is : {ans}")

    @staticmethod
    def greet():
        print("Hello how are you ")
a=int(input("Provide a number"))
Number=Calculator(a)
Number.square()
Number.cube()
Number.square_root()
