
# print("Hello Credence...")
# ##write("Hello Credence...")  ## we cant execute function before defination

# #User defined funtion
# def write():            # Defination of funtion
#     print("Hello Credence.. from write() function")     # Funtion body
#     print("Hello Credence...")
#     print("Hello Credence...") # end of body

# print("Hello Credence...") # out of function body


##-----------------------------------------------------------

# write()                 #Function Call/function execution
# write()                 #Function Call/function execution
# write()                 #Function Call/function execution
# write()                 #Function Call/function execution

# #### ----------------------------------------------------------------------------

# ### user defined function 
# print("hello cedenNce")     #hello cedenNce


# def printInUpper(valueInput):
#     print(valueInput.upper())

# ##printInUpper() #Invalid funtion call #TypeError: printInUpper() missing 1 required positional argument: 'valueInput'
# printInUpper("Hello Credence")      # HELLO CREDENCE
# printInUpper("Hello Karan")      # HELLO CREDENCE
# printInUpper("Hello Devendra")      # HELLO CREDENCE
# printInUpper("Hello Prachi")      # HELLO CREDENCE

# ### ----------------------------------------------------------------


# def printInUpper(valueInput : str):  # parameterized function 
#     print(valueInput.upper())

# ##printInUpper() #Invalid funtion call #TypeError: printInUpper() missing 1 required positional argument: 'valueInput'
# printInUpper("Hello Credence")      # HELLO CREDENCE


# ### -----------------------------------------------------------------------
# print("hello")      # without return funtion
# len("hello")        #  with retun value function


# ## Funtion with return value
# def printInUpper(valueInput : str):  # parameterized function 
#     return valueInput.upper()

# ##printInUpper() #Invalid funtion call #TypeError: printInUpper() missing 1 required positional argument: 'valueInput'
# result = printInUpper("Hello Credence")      # holding output/return value in result variable
# print(result)

# ###----------------------------------------------------------------------------------


# ## Funtion with return value
# def printInUpper(valueInput : str = "Hello Credence default"):  # parameterized function 
#     return valueInput.upper()

# ##printInUpper() #Invalid funtion call #TypeError: printInUpper() missing 1 required positional argument: 'valueInput'
# result = printInUpper()      # holding output/return value in result variable 
# print(result)       # HELLO CREDENCE DEFAULT

# print(printInUpper("Hello Karan"))  # HELLO KARAN

# ###----------------------------------------------------------------------------------

print("hello", end=' ')
print("hello", end=' ')
print("hello")
print("hello")


 
##-------------------------------------------------------
def giveInUppper(value:str, value2:str):
    '''
    giveInUpper description
    value:str
    return int
    '''
    return value.upper() + value2.upper()

# print(giveInUppper("Hello",''))

# print(giveInUppper("Hello", "Credence"))
### --------------------------











