import distutils

aValue = 10 

# print(type(aValue))     # <class 'int'>
# aValue2 = str(aValue)   # typecasting # it will convert any datatype to string

# print(type(aValue))     #<class 'int'>
# print(type(aValue2))    # <class 'str'>

# -------------------------------------------------------------

# aValue = '10'   # <class 'str'>
# aValueOfDevendra2 = int(aValue)
# print(type(aValue))     #<class 'str'>
# print(type(aValueOfDevendra2))    # <class 'int'>

# ------------------------------------------------
# aValue = '10s'   # <class 'str'>
# aValue2 = int(aValue)   #typecasting # it will convert only if possible (valid integer)
# print(type(aValue))     #<class 'str'>
# print(type(aValue2))    # <class 'int'>

#---------------------------------------------------
# aValue = '10.5'   # <class 'str'>
# aValue2 = int(aValue)   #typecasting # it will convert only if possible (valid integer)
# print(type(aValue))     #<class 'str'>
# print(type(aValue2))    # <class 'int'>

#---------------------------------------------------

# aValue = '10.5'   # <class 'str'>
# aValue2 = float(aValue)   #typecasting # it will convert only if possible (valid integer)
# print(type(aValue))     #<class 'str'>
# print(type(aValue2))    # <class 'float'>

#---------------------------------------------------


# aValue = 10.5   # <class 'float'>
# aValue2 = int(aValue)   #typecasting # it will convert only if possible (valid integer)
# print(type(aValue))     #<class 'float'>
# print(type(aValue2))    # <class 'int'>

#---------------------------------------------------



# aValue = True   # <class 'bool'>
# aValue2 = int(aValue)   #typecasting # it will convert only if possible (valid integer)
# print(type(aValue))     #<class 'bool'>
# print(type(aValue2))    # <class 'int'>

#---------------------------------------------------
# aValue = 'True'   # <class 'str'>
# aValue2 = bool(aValue)   #typecasting # 
# print(type(aValue))     #<class 'str'>
# print(type(aValue2))    # <class 'bool'>

# #---------------------------------------------------\
# aValue = 'true'   # <class 'str'>
# aValue2 = bool(aValue)   #typecasting # 
# print(type(aValue))     #<class 'str'>
# print(type(aValue2))    # <class 'bool'>

# #------------------------------------------------------
# aValue = '1'   # <class 'str'>
# aValue2 = bool(aValue)   #typecasting # 
# print(type(aValue))     #<class 'str'>
# print(type(aValue2))    # <class 'bool'>

# ------------------------------------------------

# aValue = '10.5'   # <class 'str'>
# aValue = float(aValue)
# aValue = int(aValue)   #typecasting # it will convert only if possible (valid integer)
# print(type(aValue))     #<class 'int'>
# ------------------------------------------------

# print(type(int(float('10.5')))) #<class 'int'>

#----------------------------------------
# int()
# float()
# str()
# bool()


# a = None
# b = None
# c = 0
## ------------------------------------------

# aBool = 'False'
# aBoolType = bool(aBool)
# print(type(aBoolType))  # bool
# print(aBoolType)        # True


# aBool = ''
# aBoolType = bool(aBool)
# print(type(aBoolType))  # bool
# print(aBoolType)        # False

# ---------------------------------------------------

# aBool = 'False'
# aBoolType = eval(aBool)
# print(type(aBoolType))  # bool
# print(aBoolType)        # False


##print(bool(distutils.util.strtobool("False "))) "On", "Off", '1', '0', 'Yes', 'No' 




