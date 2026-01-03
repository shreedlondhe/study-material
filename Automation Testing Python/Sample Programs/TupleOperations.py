
# aTuple = (1, "Red", 60,'Credence', 'Pune', 50, "Red", 'Pune')

# print(aTuple)
# #  ------------------------------------

# #print(aTuple.count())   #TypeError: tuple.count() takes exactly one argument (0 given)

# print(aTuple.count('Red')) #  2

# # ===========================================

# tempIndex = aTuple.index('Red')     # 
# print("Index of first 'Red' : ", tempIndex)     # Index of first 'Red' :  1

# tempIndex = aTuple.index('Red',tempIndex+1)     # 
# print("Index of Second 'Red' : ", tempIndex)     # Index of first 'Red' :  6



# tempIndex = aTuple.index('Pune')     # 
# print("Index of first 'Pune' : ", tempIndex)     # Index of first 'Pune' :  4

# tempIndex = aTuple.index('Pune',tempIndex+1)     # 
# ##print("Index of Second 'Pune' : ", tempIndex)     # Index of first 'Pune' :  7
#print(f"Index of Second 'Pune' : {tempIndex}")     # Index of first 'Pune' :  7  # print("Index of Second 'Pune' : ", tempIndex) 

# #####print(f"Index of Second 'Pune' : {aTuple.index('Pune',tempIndex+1)}")    


# # ----------------------------------------------------------

aTuple = (1, "Red", 60,'Credence', 'Pune', 50, "Red", 'Pune')

# tempIndex = aTuple.index('Mumbai')     # 
# print("Index of first 'Mumbai' : ", tempIndex)     # Index of first 'Pune' :  4

# # ------------------------------------------------------------------

print(len(aTuple))


aTuple = (1, 'Pune', "Red", 60,'Credence', 'Pune', 50, "Red", 'Pune')

tempIndex = aTuple.index('Pune')     # 
print("Index of first 'Pune' : ", tempIndex)     # Index of first 'Pune' :  4

tempIndex = aTuple.index('Pune',tempIndex+1)     # 
##print("Index of Second 'Pune' : ", tempIndex)     # Index of first 'Pune' :  7
print(f"Index of Second 'Pune' : {tempIndex}")     # Index of first 'Pune' :  7  # print("Index of Second 'Pune' : ", tempIndex) 

tempIndex = aTuple.index('Pune',tempIndex+1)     # 
##print("Index of Second 'Pune' : ", tempIndex)     # Index of first 'Pune' :  7
print(f"Index of third 'Pune' : {tempIndex} : K :  {aTuple}")     # Index of first 'Pune' :  7  # print("Index of Second 'Pune' : ", tempIndex) 



