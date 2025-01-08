#create a class pets from class Animals and further create a class Dog from Pets .Add method bark to class

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhow Bhow")

d=Dog()
d.bark()
