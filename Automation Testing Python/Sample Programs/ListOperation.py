
# colorList = ['Red', 'Green', 'Blue', 'Orange', "Yellow", "white"]

# numList = [10, 4,2,33,88,3,0]
# print(numList)      #[10, 4, 2, 33, 88, 3, 0]

# # Sort to list

# numList.sort()
# print(numList)      #[0, 2, 3, 4, 10, 33, 88] 


# # Decending
# numList.sort(reverse=True)
# print(numList)      #[88, 33, 10, 4, 3, 2, 0]


# # -------------------------------------------
# strTemp = "welcome"
# strTemp2 = strTemp.replace('w','z')

# virtualTemp = "Zelcome"

# # -----------------------------------------

# numList = [10, 4,2,33,88,3,0]
# print(numList.reverse())  #None
# print(numList)              #[0, 3, 88, 33, 2, 4, 10]

# # ------------------------------------------------

# colorList = ['Red', 'Green', True, 'Orange', 1 , 20.5, None]
# colorList.sort()
# print(colorList)


# colorList = ['Red', 'Green', 10, 'Orange', 1 , 20.5]
# colorList.sort()
# print(colorList)


from os import remove
from queue import PriorityQueue


colorList = ['Red', 'Green', 'Orange']
colorList.sort()
print(colorList)        # ['Green', 'Orange', 'Red']



colorList = [True, False, True]
colorList.sort()
print(colorList)        # [False, True, True]  
# False = 0
# True = 1


# ----------------------------------------------

# append 

# tempList = [0, 2, 3, 4, 10, 33, 88] 
# tempList.append(100)

# print(tempList) # [0, 2, 3, 4, 10, 33, 88, 100]

# # insert 
# tempList = [0, 2, 3, 4, 10, 33, 88] 
# tempList.insert(3,100)

# print(tempList) # [0, 2, 3,100, 4, 10, 33, 88] 


# --------------------------------------------------------

# it work with index -- input index
tempList = [0, 2, 3, 4, 10, 33, 88] 

# print(tempList.pop())       # 88  # default last element 
# print(tempList.pop(3))       # 4
# print(tempList)       # [0, 2, 3, 10, 33]


print(tempList.pop(5),tempList.pop(2))       #33 3
print(tempList)             #[0, 2, 4, 10, 88]
#print(tempList.pop())       # 88  # default last element 
##

# ------------------------------

#  Remove

# tempList = [0, 2, 3, 4, 10, 33, 88] 

# temp = tempList.remove(88)  
# print(temp)     #None
# print(tempList)     #[0, 2, 3, 4, 10, 33]

# -------------------------------------


colorList = ['Red', 'Green', 10, 'Orange', 1 , 20.5]
colorList = ['Red', 'Green', '10', 'Orange', "1" , "20.5"]

sorted(colorList, key=str)
##print(sorted(colorList))

print(sorted(colorList, key=str))     #accending  # [1, 10, 20.5, 'Green', 'Orange', 'Red']


print(sorted(colorList, key=str,reverse=True)) #['Red', 'Orange', 'Green', 20.5, 10, 1]









