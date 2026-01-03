# 4 = 4 * 3 * 2 * 1 
# 5 = 5 * 4 * 3 * 2 * 1

# print("Factorial of 5 : ", 5 * 4 * 3 * 2 * 1)

# ## -----------------------------------------------------
# # Function start
# def factorial(): # Fun def 
#     print("factorial code")
#     #other statements
#     #other code
# #Function end

# factorial()     # function call 


# ## -----------------------------------------------------
# # Function start
# def factorial(): # Fun def 
#     print("factorial code")
#     #other statements
#     #other code
#     factorial()
# #Function end

# factorial()     # function call 

# ## --------------------------------------------

# Factorial program with recursion 
# 5 = 5 * 4 * 3 * 2 * 1

print("Factorial of 8 : ", 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)

def factorial(n : int):
    if n <= 1:     # n == 1 or n == 0
        return 1
    else: 
        return n * factorial(n-1)       #n * (n-1) * (n-2) * (n-3) * (n-4)

# 3 * 2 * 1

## -- function call 
num = -2
fact = factorial(num)
print(f"Factorial of {num} : {fact}")

# 3 * 2 * 1

