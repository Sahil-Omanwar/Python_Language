#instance attribute is always preferred over class
class Employee:
    language="Py"
    salary=1303030

harry=Employee()
#Language and salary are class attribute
harry.language="C++"#instance attribte
print(harry.language,harry.salary)