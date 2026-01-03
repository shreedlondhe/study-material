
## Class constructors
## Default constructors




class StudentDetails:
    def __init__(self):         #Default constructor
        self.name = "Sanjeev"
        self.address = "Mumbai"
    
objStud = StudentDetails()
print(f"Student details : Name = {objStud.name}, address ={objStud.address}")   #Student details : Name = Sanjeev, address =Mumbai
    
### -------------------------------------------------------------------------------------------
### parameterized constructor


class Addition: 
    def __init__(self, first, second) -> None:  # parameterized constructor
        self.firstNum = first
        self.secondNum = second

    def getResult(self) -> int:
        return self.firstNum + self.secondNum 



# addObj = Addition()
# result = addObj.getResult()
# print("Addition of 2 nums = ",  result)

addObj = Addition(100, 300)
result = addObj.getResult()
print("Addition of 2 nums = ",  result)  # Addition of 2 nums =  400

# --------------------------------------------------------------------
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

addObj = Addition(num1, num2)
result = addObj.getResult()
print("Addition of 2 nums = ",  result)  # Addition of 2 nums =  400
