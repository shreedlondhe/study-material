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

    @staticmethod
    def getCompanyDetails():
        print("Company Credence is located at Pune")

    @staticmethod
    def isAdult(age) -> bool:
        if(age >= 18):
            return True
        else: 
            return False
# ----------------------------------------------------

Employee.getCompanyDetails()    #Company Credence is located at Pune
print(Employee.isAdult(20))     # True

