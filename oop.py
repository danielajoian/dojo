# classes
class Employee:

    def __init__(self, name, salary):
         self.name = name 
         self.salary = salary 

    def printName(self):
        print("The name of the employee is ", self.name)

    def printSalary(self):
        print("The sum of the salary is ", self.salary)

John = Employee("John", 5300)
John.printName()
John.printSalary()