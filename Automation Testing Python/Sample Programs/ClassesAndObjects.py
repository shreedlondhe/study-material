# ### Function Approach  ## Without class
# id = 1001
# name = 'Mayur'
# address = 'Pune'
# salary = "10000000000"

# def getEmployeeDetails():
#     print(f"Employee Details : id = {id}, name = {name}, address = {address}, salary = {salary}")


# getEmployeeDetails()
# getEmployeeDetails()
# getEmployeeDetails()
# getEmployeeDetails()
# getEmployeeDetails()
# getEmployeeDetails()
# getEmployeeDetails()

# ###-----------------------------------------------------------------------------

### With class approach 
class Employee: # defining class
    id = 1001       # class attribute
    name = 'Mayur'  # class attribute
    address = 'Pune'    # class attribute
    salary = "10000000000"  # class attribute

    def getEmployeeDetails(self):   # defining method 
        print(f"Employee Details : id = {self.id}, name = {self.name}, address = {self.address}, salary = {self.salary}")

    def getEmployeeSalary(self):   # defining method 
        return self.salary  # return salary value from method 

    def getCompanyDetails():
        print("Company Credence is located at Pune")
# ----------------------------------------------------

###getEmployeeDetails()        # we can not call class inside method without using class/object of perticular class

#Employee.getEmployeeDetails()   #TypeError: getEmployeeDetails() missing 1 required positional argument: 'self'

emp = Employee()        #  object creation of Employee class
####Employee.getEmployeeDetails(emp)  # 1st Approach  # Call method wiht class name by passing object in self parameter      # Employee Details : id = 1001, name = Mayur, address = Pune, salary = 10000000000

emp.getEmployeeDetails()     # 2nd Approach #   calling method of class by emp 

# print(f"Employee Details : id = {emp.id}, name = {emp.name}, address = {emp.address}, salary = {emp.salary}")

# print(f"Employee Details : id = {Employee.id}, name = {Employee.name}, address = {Employee.address}, salary = {Employee.salary}")


# Employee.getCompanyDetails()        #Company Credence is located at Pune
#emp.getCompanyDetails()             #TypeError: getCompanyDetails() takes 0 positional arguments but 1 was given

## ---------------------------------------------------------------

class TempEmployee: # defining class
    id = 2001       # class attribute
    name = 'Sanjeev'  # class attribute
    address = 'Mumbai'    # class attribute
    salary = "20000000000"  # class attribute

    def getEmployeeDetails(self):   # defining method 
        print(f"Employee Details : id = {self.id}, name = {self.name}, address = {self.address}, salary = {self.salary}")

    def getEmployeeSalary(self):   # defining method 
        return self.salary  # return salary value from method 

    def getCompanyDetails():
        print("Company Credence is located at Pune")
# ----------------------------------------------------

emp1 = TempEmployee()
emp1.getEmployeeDetails()
