
aSet = {1, 8, 10 ,4, 6}

# # print(f"aSet values : {aSet}")  # aSet : {1, 8, 10 ,4, 6}
# # aSet.remove(8)
# # print("aSet values : ", aSet)


print(f"aSet values : {aSet}")  # aSet : {1, 8, 10 ,4, 6}
poppedElement = aSet.pop()
print("aSet values : ", aSet, " after popping element : ", poppedElement)
print(f"aSet values : {aSet} after popping element: {poppedElement}")

# ----------------------------------------------------

#  --------------------------------------------------------------------------------------

# # Union 

# aSet = {1, 4, 8, 9 ,3}      # set
# aSet2 = {4, 8, 10, 20}     #set 

# tempSet = aSet.union(aSet2)       

# print("aSet : ", aSet)  # aSet :  {1, 3, 4, 8, 9}
# print("aSet2 : ", aSet2)    # aSet2 :  {8, 10, 4, 20}
# print("tempSet : ", tempSet)    # tempSet :  {1, 3, 4, 8, 9, 10, 20}

# ---------------------------------------------------------------------
# intersection
aSet = {1, 4, 8, 9 ,3}      # set
aSet2 = {4, 8, 10, 20}     #set 

tempSet = aSet.intersection(aSet2)       

print("aSet : ", aSet)  # aSet :  {1, 3, 4, 8, 9}
print("aSet2 : ", aSet2)    # aSet2 :  {8, 10, 4, 20}
print("tempSet : ", tempSet)    # tempSet :  {8, 4}

# -----------------------------------------------------------------------------------









