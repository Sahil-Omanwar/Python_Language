class Student:

    language="py"
    salary=1200000
    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary


    def getInfo(self):
         print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


#language and salary are class attribute and name is object or instance attribute
#instance attribute is always preferred over class




pranav=Student("Pranav","English",2900000)
print(pranav.name)
print(pranav.language)
print(pranav.salary)
print(pranav.getInfo())
print(pranav.greet())
