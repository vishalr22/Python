'''
Class Variables:
They are defined at the class level and are shared among all instances of the class.
They are defined outside of any method and are usually used to store information that is common to all instances of the class.
It can be accessed via classname.variable_name or self.class_variable_name.


Instance Variables:
Instance variables are defined at the instance level and are unique to each instance of the class.
They are defined inside the init method and are usually used to store information that is specific to each instance of the class.
They are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name.
'''


class Employee:
    companyName = 'Apple'
    employeeNo = 0

    def __init__(self, name, employee_id):
        self.name = name
        self.id = employee_id
        Employee.employeeNo =+ 1

    def show_details(self):
        print(f"The employee number {Employee.employeeNo} is {self.name}. His employee id is {self.id} from {Employee.companyName} company.")


emp1 = Employee('Vishal', 1)
emp1.show_details()
emp1.companyName = 'Google'  # emp1 will not change the value as companyName is a class variable
emp1.show_details()

Employee.companyName = 'Capgemini'  # value will be changed
print(Employee.companyName)
emp1.show_details()
