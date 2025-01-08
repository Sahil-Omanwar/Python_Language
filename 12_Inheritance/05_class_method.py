class Employee:
    a=1
    @classmethod
    def show(cls):##we use cls instead of self
        print(f"The class attribute of a is {cls.a}")


e=Employee()
e.a=45
e.show()