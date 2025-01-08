#create a class employee and add salary and increment properties to it
#write a method salaryAfterIncrement method with @property decorator woth a setter changes the value of increment based on salary

class Employee:
    salary=234
    increment=20

    @property
    def salaryAfterIncrement(self):
        return (self.salary+self.salary*(self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=((salary/self.salary)-1)*100



e=Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=280.8
print(e.increment)