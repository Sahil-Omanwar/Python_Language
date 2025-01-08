class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

    def hello(self):
        print("How are you Employee")



# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")
#
#     def showLanguage(self):
#         print(f"The name is {self.name} ans he is good woth {self.language} language")
class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language {self.language}")

    def hello(self):
        print("How are you coder")

class Programmer(Employee,Coder):##In case of ambiguity the properties of employee are shown as it is defined first
    company = "ITC Infotech"

    def __init__(self, name, salary, ):
        self.name=name
        self.salary=salary


    # def showLanguage(self):
    #     print(f"The name is {self.name} and he is good with {self.language} language")



a=Employee("Sahil",50000)
b=Programmer("Pranav",80000)
print(a.company,b.company)
a.show()
b.show()
b.printLanguage()
b.hello()
