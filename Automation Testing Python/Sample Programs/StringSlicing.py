# string slicing

aVariable = "Welcome"

# get perticular character with string slicing/indexing  
# print(aVariable)    # Welcome
# print(aVariable[1]) # e
# print(aVariable[0]) # W

# print(aVariable[3])
# print(aVariable[6])

# aInputString = input("Enter a string : ") #karansingh
# print("First Char : ", aInputString[0])
# print("Last Char index: ", len(aInputString)-1)
# print("Last Char : ", aInputString[len(aInputString)-1])


# ## Reverse indexing 

# aVariable = "Welcome"

# # get perticular character with string slicing/indexing  
# print(aVariable)    # Welcome
# print("Last Char : ", aVariable[-1]) # Last Char :  e
# print("First Char : ",aVariable[-7]) # First Char :  W



# ---------------------------------------------------------------------

aVariable = "Welcome"

# #Wel
# print(aVariable[0],aVariable[1],aVariable[2])   #W e l
# print(aVariable[0]+aVariable[1]+aVariable[2]) # Wel

# print(aVariable[0,1,2])     # ???  invalid syntax

# # index range
# print(aVariable[0:1])   # We ?? W
# print(aVariable[0:2])   # We
# print(aVariable[0:4])   # We ?? Welc

# print(aVariable[3:4])   # c 
# print(aVariable[3:7])   # come 
# --------------------------------------------------------

# print(aVariable[0:-1])  # Welcom
# print(aVariable[0:0])  # 

# print(aVariable[0:])  # Welcome
# print(aVariable[:])  # Welcome

# ----------------------------------------------------------

# print(aVariable[0:7:1]) # Welcome
# print(aVariable[0:7:2]) # Wloe
# print(aVariable[0:7:3]) # Wce
# print(aVariable[0:7:0]) # Invalid slice step can not be zero


# ----------------------------------------------------

# a = aVariable[0]    # a = 'W'
# b ='Z'
# aVariable = b       # aVariable = 'Z'
# print('aVariable : '+ aVariable, " b : " + b)

aVariable = "Welcome"
b = 'Z'

aVariable[0] = b       # aVariable = 'Z'
print('aVariable : '+ aVariable, " b : " + b)   #TypeError: 'str' object does not support item assignment

# string is immutable   = can not be changed or modified .. 























