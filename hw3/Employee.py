'''Medium Question  (5 points)

2.  Create a class called Employee with attributes 
name and salary. Implement a method within the class that 
increases the salary of the employee by a given percentage. 
Instantiate an object of the Employee class with name = "John" 
and salary = 5000, increase the salary by 10%, and print the updated 
salary. '''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def earning(self, percentage):
        percentage = percentage / 100
        return (self.salary * percentage) + self.salary

employee = Employee('John', 5000)

print(employee.earning(10))

# https://chatgpt.com/share/6aa60c7f-9054-83ea-905c-18c26027eb05

