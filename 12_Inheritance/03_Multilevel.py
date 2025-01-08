class Employee:
    a=1


class Programmer(Employee):
   a=6
   b=2


class Manager(Programmer):
    c=3

one=Manager()
print(one.a)