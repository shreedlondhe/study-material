
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

    def getEmployeeDetailsWithBonus(self):   # defining method 
        print(f"Employee Details : id = {self.id}, name = {self.name}, address = {self.address}, salary = {self.salary}, Bonus = {self.bonus}")

# # ----------------------------------------------------
# # execute methods with default value of multiple object 
# emp = Employee()        #  object creation of Employee class
# emp.getEmployeeDetails()     # 2nd Approach #   calling method of class by emp 

# emp2 = Employee()        #  object creation of Employee class
# emp2.getEmployeeDetails()     # 2nd Approach #   calling method of class by emp 

# emp3 = Employee()
# emp3.getEmployeeDetails()

# # ----------------------------------------------------
# execute methods with default/updated values of multiple object 
emp = Employee()        #  object creation of Employee class
emp.getEmployeeDetails()     # 2nd Approach #   calling method of class by emp 

emp2 = Employee()        #  object creation of Employee class
emp2.getEmployeeDetails()     # 2nd Approach #   calling method of class by emp 
emp2.id= 2001
emp2.name = "Karan"
emp2.address= "Achalpur"
emp2.salary = "30000000"
emp2.getEmployeeDetails()     # 2nd Approach #   calling method of class by emp 


emp3 = Employee()        #  object creation of Employee class
emp3.getEmployeeDetails()     # Employee Details : id = 1001, name = Mayur, address = Pune, salary = 10000000000
emp3.name = "Devendra"
emp3.getEmployeeDetails()     # Employee Details : id = 1001, name = Devendra, address = Pune, salary = 10000000000

## -----------------------------------------------------------

Employee.address = "Mumbai"     # changes will be made in all the Employee class objects but but only in those objects where attribute was never changed/modified 

emp.getEmployeeDetails()    #Employee Details : id = 1001, name = Mayur, address = Mumbai, salary = 10000000000
emp2.getEmployeeDetails()   #Employee Details : id = 2001, name = Karan, address = Achalpur, salary = 30000000
emp3.getEmployeeDetails()   #Employee Details : id = 1001, name = Devendra, address = Mumbai, salary = 10000000000


### ------------------------------------------------------------


emp2.bonus  = 100000
emp2.getEmployeeDetails()   #Employee Details : id = 2001, name = Karan, address = Achalpur, salary = 30000000
emp2.getEmployeeDetailsWithBonus()  #Employee Details : id = 2001, name = Karan, address = Achalpur, salary = 30000000, Bonus = 100000
print(f"Employee details : name {emp2.name}, bonus = {emp2.bonus}")     #Employee details : name Karan, bonus = 100000
###emp.getEmployeeDetailsWithBonus()   #AttributeError: 'Employee' object has no attribute 'bonus'



