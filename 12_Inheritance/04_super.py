##Super is used so that the construtor of base class also works

class Employee:
    def __init__(self):
        print("Constructor of Employee")

    a=1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b=2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3

obj1=Manager()
