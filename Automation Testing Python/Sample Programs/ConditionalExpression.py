# if statement 

# a = 20
# if(a > 10):  ##True
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
# print("if block completed")


# a = 5
# if(a > 10):     # false
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")

# print("if block completed")


# # -------------------------------------------------

# ###if-else state

# a = 5
# if(a > 10):     # false
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
# else:
#     print("a is lesser than 10")  

# print("if block completed")

# ## -----------------------------------------
# ### if-elif statements

# a = 5
# if(a > 10):     # false
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
# elif(a < 10):
#     print("a is lesser than 10")  
    
# print("if block completed")

# ## -----------------------------------------
# ### if-elif-else statements

# a = 10
# if(a > 10):     # false
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
# elif(a < 10):   # false
#     print("a is lesser than 10") 
# else: 
#     print("a is equal to 10") 
    
# print("if block completed")

# ###------------------------------------------------------
# ## if-elif-elif-else

# a = 10
# if(a > 10):     # false
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
#     print("a is greater than 10")
# elif(a < 10):   # false
#     print("a is lesser than 10") 
# elif(a == 10):   # true
#     print("a is equal to 10") 
# else: 
#     print("Dont know...") 

# ## -----------------------------------------------------------

a = int(input("Enter a number: "))
b = 10
if(a > 10):     # false
    if(b  == 10 ):
        print("a is greater than 10")
        print("a is greater than 10")
    print("a is greater than 10")
    print("a is greater than 10")
    print("a is greater than 10")
elif(a < 10 and a == b):   # false
    print("a is lesser than 10") 
elif(a == 10):   # true
    print("a is equal to 10") 
else: 
    print("Dont know...") 
