
import atexit


aTemp = "Welcome"   # Does it ends with 'me'?

print(aTemp[-2:])

length = len(aTemp)
aTemp.endswith('me')
print(aTemp.endswith("me"))  # True 


print(aTemp.startswith('we')) #False
print(aTemp.startswith('We')) #True


# Count number of char present in string 

aTempCount = aTemp.count('c')
print(aTempCount)

aTempCount = aTemp.count('e')   #2
print(aTempCount)

aTempCount = aTemp.count('z')   #2
print(aTempCount)

print(aTemp.count('e', 2)) #1
print(aTemp.count('e', 2,3)) #0
print(aTemp.count('e', 2,6)) #0     
print(aTemp.count('e', 2,7)) #1     


#print(aTemp.count()) # TypeError: count() takes at least 1 argument (0 given)

# aTemp = "Welcome"   # 
 
# # space
# print(aTemp.count(''))       # 8 Welcome
# print(aTemp.count('',2,7))   #6
# print(aTemp.count(' '))       # 0


# #  Capitalize
# aTemp = "weLcoMe"
# newValue = aTemp.capitalize()
# print(newValue)  #Welcome
# print(aTemp)    #weLcoMe



# # Find function
# aTemp = "Welcome"
# print("index of 'come'", aTemp.find('come'))  # 3
# print("index of 'Come'", aTemp.find('Come')) # -1
# print("I am Pushpa", aTemp.find('dfs')) # -1
# print(aTemp.find('dfs')) # -1

# # 



# 
aTemp =  "I am don don don"
##aTemp =  "I am Pushpa Pushpa Pushpa"

aTemp = aTemp.replace('don', 'Pushpa')
#print(aTemp222)
print(aTemp)



'fsa\'df'















