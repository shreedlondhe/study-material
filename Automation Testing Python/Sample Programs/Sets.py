from multiprocessing.pool import AsyncResult
from traceback import print_tb


aTuple = (1, 4,7,9,3,0) # valid tuple
aTuple = 1, 4,7,9,3,0 # valid tuple
aList = [1, 4,7,9,3,0]  # valid list

aDictionary = {1:100, 4:"sd", 7:True,  9:False, 3:0, True: 'Credence'}  # valid Dictionary 
print(type(aDictionary))        #<class 'Dist'>
print(aDictionary[1])           # Credence

aSet = {1, 4,7,9,3,0,4,7}  # 
print(aSet) #{0, 1, 3, 4, 7, 9}
print(type(aSet)) ##<class 'set'>


aSet = {1, "4",7,9.3,3,0,4,True}  # 
print(aSet) #{0, 1, 3, 4, 7, 9.3, '4'}
print(type(aSet)) ##<class 'set'>

# ----------------------------------------------





