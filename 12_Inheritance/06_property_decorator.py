class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


    #encapsulation and abstraction
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
    @name.deleter
    def name(self):
        print("Delete name")
        self.fname=None
        self.lname=None

e=Employee()
e.a=45 
e.name="Sahil Omanwar"
print(e.fname,e.lname)
e.show()
del e.name