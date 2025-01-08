#In this file class attributes are defined
class Employee:
    language="Py"
    salary=130303

harry=Employee()
print(harry.language,harry.salary)#class attribute
harry.name="Harry"##object attribute
print(harry.name)