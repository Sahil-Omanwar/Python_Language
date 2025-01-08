class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")
# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")
#
#     def showLanguage(self):
#         print(f"The name is {self.name} ans he is good woth {self.language} language")

class Programmer(Employee):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")



a=Employee("Sahil",50000)
b=Programmer("Pranav",80000,"Hindi")
print(a.company,b.company)
a.show()
b.show()
